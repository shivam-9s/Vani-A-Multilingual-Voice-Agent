import os
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_DATASET = "datasets/cleaned/training_data_clean.csv"

REPORT_FILE = "datasets/reports/dataset_conflicts.csv"

TEXT_COLUMNS = [
    "text",
    "sentence",
    "query",
    "utterance"
]

INTENT_COLUMN = "intent"


# ==========================================================
# Detect Text Column
# ==========================================================

def detect_text_column(df):

    for col in TEXT_COLUMNS:
        if col in df.columns:
            return col

    return None


# ==========================================================
# Main
# ==========================================================

def main():

    print("=" * 70)
    print("VANI DATASET REPAIR")
    print("=" * 70)

    df = pd.read_csv(INPUT_DATASET)

    text_column = detect_text_column(df)

    if text_column is None:
        print("❌ No valid text column found.")
        return

    print(f"\nDataset Loaded : {INPUT_DATASET}")
    print(f"Samples : {len(df)}")

    # ------------------------------------------------------
    # Detect Conflicts
    # ------------------------------------------------------

    grouped = (
        df.groupby(text_column)[INTENT_COLUMN]
        .agg(list)
        .reset_index()
    )

    conflicts = []

    for _, row in grouped.iterrows():

        intents = list(sorted(set(row[INTENT_COLUMN])))

        if len(intents) > 1:

            conflicts.append({

                "text": row[text_column],

                "intent_count": len(intents),

                "intents": ", ".join(intents)

            })

    conflict_df = pd.DataFrame(conflicts)

    os.makedirs("datasets/reports", exist_ok=True)

    conflict_df.to_csv(

        REPORT_FILE,

        index=False

    )

    print("\nConflict Report Generated")

    print(REPORT_FILE)

    print(f"\nTotal Conflicting Text : {len(conflict_df)}")

    # ------------------------------------------------------
    # Preview
    # ------------------------------------------------------

    if len(conflict_df):

        print("\nFirst 10 Conflicts\n")

        print(conflict_df.head(10).to_string(index=False))

    else:

        print("\nNo conflicting samples found.")

    print("\nRepair Report Generated Successfully.")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":

    main()