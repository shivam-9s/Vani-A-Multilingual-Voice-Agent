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
# Statistics
# ----------------------------------------

print("=" * 60)
print("VANI DATASET REPORT")
print("=" * 60)

print(f"Total Samples        : {len(df)}")
print(f"Total Intents        : {df['intent'].nunique()}")
print(f"Unique Sentences     : {df['text'].nunique()}")

duplicates = df.duplicated().sum()

print(f"Duplicate Rows       : {duplicates}")

missing = df.isnull().sum().sum()

print(f"Missing Values       : {missing}")

print()

print("=" * 60)
print("Intent Distribution")
print("=" * 60)

counts = df["intent"].value_counts().sort_index()

for intent, count in counts.items():
    print(f"{intent:<30} {count}")

print()

print("=" * 60)

print(f"Minimum Samples / Intent : {counts.min()}")

print(f"Maximum Samples / Intent : {counts.max()}")

print(f"Average Samples / Intent : {counts.mean():.2f}")

print("=" * 60)