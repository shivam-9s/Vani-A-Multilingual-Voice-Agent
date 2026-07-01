import pandas as pd

# ----------------------------------------
# Dataset Path
# ----------------------------------------

DATASET_PATH = "datasets/intents/training_data.csv"

# ----------------------------------------
# Load Dataset
# ----------------------------------------

df = pd.read_csv(DATASET_PATH)

# ----------------------------------------
# Find Duplicate Sentences
# ----------------------------------------

duplicates = df[df.duplicated(subset=["text"], keep=False)]

print("=" * 70)
print("VANI DUPLICATE CHECKER")
print("=" * 70)

if duplicates.empty:

    print("\n✅ No duplicate sentences found.")

else:

    print(f"\n❌ Total Duplicate Rows : {len(duplicates)}\n")

    grouped = duplicates.groupby("text")

    for sentence, group in grouped:

        print("-" * 70)
        print(f"Sentence : {sentence}")
        print(f"Occurrences : {len(group)}")

        print("Intents :")

        for intent in group["intent"].tolist():

            print(f"   • {intent}")

print("\n" + "=" * 70)
print("Duplicate Check Completed")
print("=" * 70)