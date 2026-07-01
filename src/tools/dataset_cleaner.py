import os
import re
import pandas as pd

RAW_DATASET = "datasets/raw/training_data.csv"
OUTPUT_DATASET = "datasets/cleaned/training_data_clean.csv"

TEXT_COLUMNS = [
    "text",
    "sentence",
    "query",
    "utterance"
]

INTENT_COLUMN = "intent"


def detect_text_column(df):

    for col in TEXT_COLUMNS:
        if col in df.columns:
            return col

    return None


def clean_text(text):

    text = str(text)

    text = text.strip()

    text = re.sub(r"\s+", " ", text)

    return text


def main():

    print("=" * 70)
    print("VANI DATASET CLEANER")
    print("=" * 70)

    df = pd.read_csv(RAW_DATASET)

    print(f"\nOriginal Samples : {len(df)}")

    text_column = detect_text_column(df)

    if text_column is None:
        print("No valid text column found.")
        return

    # -----------------------------
    # Clean text
    # -----------------------------

    df[text_column] = df[text_column].apply(clean_text)

    df[INTENT_COLUMN] = (
        df[INTENT_COLUMN]
        .astype(str)
        .str.strip()
    )

    # -----------------------------
    # Remove blank rows
    # -----------------------------

    before = len(df)

    df = df[
        df[text_column] != ""
    ]

    df = df[
        df[INTENT_COLUMN] != ""
    ]

    print(f"Removed Blank Rows : {before-len(df)}")

    # -----------------------------
    # Remove exact duplicate rows
    # -----------------------------

    before = len(df)

    df = df.drop_duplicates()

    print(f"Removed Duplicate Rows : {before-len(df)}")

    # -----------------------------
    # Save
    # -----------------------------

    os.makedirs("datasets/cleaned", exist_ok=True)

    df.to_csv(
        OUTPUT_DATASET,
        index=False
    )

    print("\nSaved Clean Dataset")

    print(OUTPUT_DATASET)

    print(f"\nFinal Samples : {len(df)}")

    print("\nDataset Cleaning Completed Successfully.")


if __name__ == "__main__":

    main()