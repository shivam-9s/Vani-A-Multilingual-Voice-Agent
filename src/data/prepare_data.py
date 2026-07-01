import os
import pandas as pd

from sklearn.model_selection import train_test_split

from src.models.config import (
    CLEAN_DATASET,
    TRAIN_FILE,
    TEST_FILE,
    RANDOM_SEED
)

# =====================================================
# Prepare Train/Test Dataset
# =====================================================

def main():

    print("=" * 60)
    print("Preparing Dataset")
    print("=" * 60)

    # -----------------------------------------
    # Load Clean Dataset
    # -----------------------------------------

    df = pd.read_csv(CLEAN_DATASET)

    print(f"\nLoaded Dataset : {CLEAN_DATASET}")

    print(f"Total Samples : {len(df)}")

    # -----------------------------------------
    # Remove Missing Values
    # -----------------------------------------

    df.dropna(inplace=True)

    # -----------------------------------------
    # Remove Duplicate Rows
    # -----------------------------------------

    df.drop_duplicates(inplace=True)

    # -----------------------------------------
    # Shuffle Dataset
    # -----------------------------------------

    df = df.sample(
        frac=1,
        random_state=RANDOM_SEED
    ).reset_index(drop=True)

    # -----------------------------------------
    # Create Output Folder
    # -----------------------------------------

    os.makedirs(
        "datasets/processed",
        exist_ok=True
    )

    # -----------------------------------------
    # Train Test Split
    # -----------------------------------------

    train_df, test_df = train_test_split(

        df,

        test_size=0.20,

        stratify=df["intent"],

        random_state=RANDOM_SEED

    )

    # -----------------------------------------
    # Save Files
    # -----------------------------------------

    train_df.to_csv(

        TRAIN_FILE,

        index=False

    )

    test_df.to_csv(

        TEST_FILE,

        index=False

    )

    # -----------------------------------------
    # Statistics
    # -----------------------------------------

    print("\n" + "=" * 60)

    print("Dataset Statistics")

    print("=" * 60)

    print(f"Training Samples : {len(train_df)}")

    print(f"Testing Samples  : {len(test_df)}")

    print("\nIntent Distribution\n")

    print(df["intent"].value_counts())

    print("\nTrain File")

    print(TRAIN_FILE)

    print("\nTest File")

    print(TEST_FILE)

    print("\nDataset Preparation Completed Successfully.")

# =====================================================

if __name__ == "__main__":

    main()