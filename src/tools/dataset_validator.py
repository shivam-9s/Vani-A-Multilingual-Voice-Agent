import pandas as pd
from pathlib import Path

# ==========================================================
# Configuration
# ==========================================================

DATASET = "datasets/raw/training_data.csv"

TEXT_COLUMNS = [
    "text",
    "sentence",
    "query",
    "utterance"
]

INTENT_COLUMN = "intent"


# ==========================================================
# Dataset Validator
# ==========================================================

def validate_dataset():

    print("=" * 70)
    print("VANI DATASET VALIDATOR")
    print("=" * 70)

    dataset_path = Path(DATASET)

    # ------------------------------------------------------
    # Check Dataset Exists
    # ------------------------------------------------------

    if not dataset_path.exists():
        print(f"\n❌ Dataset not found:\n{DATASET}")
        return

    df = pd.read_csv(dataset_path)

    print(f"\nDataset Loaded : {DATASET}")
    print(f"Total Samples  : {len(df)}")

    # ------------------------------------------------------
    # Detect Text Column
    # ------------------------------------------------------

    print("\nChecking Required Columns...")

    text_column = None

    for col in TEXT_COLUMNS:
        if col in df.columns:
            text_column = col
            break

    if text_column is None:
        print("❌ No valid text column found.")
        print(f"Expected one of: {TEXT_COLUMNS}")
        return

    if INTENT_COLUMN not in df.columns:
        print("❌ Missing intent column.")
        return

    print(f"✅ Text Column   : {text_column}")
    print(f"✅ Intent Column : {INTENT_COLUMN}")

    # ------------------------------------------------------
    # Missing Values
    # ------------------------------------------------------

    print("\nChecking Missing Values...")

    missing = df.isnull().sum()

    if missing.sum() == 0:
        print("✅ No missing values")
    else:
        print(missing)

    # ------------------------------------------------------
    # Empty Text
    # ------------------------------------------------------

    print("\nChecking Empty Text...")

    empty_text = (
        df[text_column]
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    print(f"Empty Text Samples : {empty_text}")

    # ------------------------------------------------------
    # Blank Intents
    # ------------------------------------------------------

    print("\nChecking Blank Intents...")

    blank_intents = (
        df[INTENT_COLUMN]
        .astype(str)
        .str.strip()
        .eq("")
        .sum()
    )

    print(f"Blank Intents : {blank_intents}")

    # ------------------------------------------------------
    # Duplicate Rows
    # ------------------------------------------------------

    print("\nChecking Duplicate Rows...")

    duplicate_rows = df.duplicated().sum()

    print(f"Duplicate Rows : {duplicate_rows}")

    # ------------------------------------------------------
    # Duplicate Text
    # ------------------------------------------------------

    print("\nChecking Duplicate Text...")

    duplicate_text = (
        df[text_column]
        .duplicated()
        .sum()
    )

    print(f"Duplicate Text : {duplicate_text}")

    # ------------------------------------------------------
    # Conflicting Sentences
    # ------------------------------------------------------

    print("\nChecking Conflicting Text...")

    conflicts = (
        df.groupby(text_column)[INTENT_COLUMN]
        .nunique()
        .reset_index()
    )

    conflicts = conflicts[
        conflicts[INTENT_COLUMN] > 1
    ]

    print(f"Conflicting Text Samples : {len(conflicts)}")

    # ------------------------------------------------------
    # Intent Distribution
    # ------------------------------------------------------

    print("\nIntent Distribution\n")

    intent_counts = (
        df[INTENT_COLUMN]
        .value_counts()
        .sort_index()
    )

    print(intent_counts)

    # ------------------------------------------------------
    # Dataset Statistics
    # ------------------------------------------------------

    print("\nDataset Statistics")

    print(f"\nUnique Intents : {df[INTENT_COLUMN].nunique()}")

    print(
        f"Minimum Samples per Intent : {intent_counts.min()}"
    )

    print(
        f"Maximum Samples per Intent : {intent_counts.max()}"
    )

    print(
        f"Average Samples per Intent : {intent_counts.mean():.2f}"
    )

    # ------------------------------------------------------
    # Final Summary
    # ------------------------------------------------------

    print("\n" + "=" * 70)
    print("VALIDATION SUMMARY")
    print("=" * 70)

    print(f"Dataset              : {DATASET}")
    print(f"Text Column          : {text_column}")
    print(f"Total Samples        : {len(df)}")
    print(f"Unique Intents       : {df[INTENT_COLUMN].nunique()}")
    print(f"Duplicate Rows       : {duplicate_rows}")
    print(f"Duplicate Text       : {duplicate_text}")
    print(f"Conflicting Samples  : {len(conflicts)}")
    print(f"Empty Text           : {empty_text}")
    print(f"Blank Intents        : {blank_intents}")

    print("\n✅ Validation Completed Successfully")


# ==========================================================
# Main
# ==========================================================

if __name__ == "__main__":
    validate_dataset()