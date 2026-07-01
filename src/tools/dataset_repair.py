import pandas as pd

# ---------------------------------------
# Dataset Path
# ---------------------------------------

DATASET_PATH = "datasets/intents/training_data.csv"

# ---------------------------------------
# Load Dataset
# ---------------------------------------

df = pd.read_csv(DATASET_PATH)

print("=" * 70)
print("VANI DATASET REPAIR TOOL")
print("=" * 70)

# ---------------------------------------
# Find conflicting labels
# ---------------------------------------

conflicts = []

grouped = df.groupby("text")

for sentence, group in grouped:

    intents = group["intent"].unique()

    if len(intents) > 1:

        conflicts.append({
            "text": sentence,
            "intents": ", ".join(intents),
            "count": len(group)
        })

# ---------------------------------------
# Display Results
# ---------------------------------------

if len(conflicts) == 0:

    print("\n✅ No conflicting labels found.")

else:

    print(f"\n⚠ Conflicting Sentences : {len(conflicts)}\n")

    for i, row in enumerate(conflicts, start=1):

        print("-" * 70)
        print(f"{i}. Sentence")
        print(row["text"])

        print("\nAssigned Intents")

        for intent in row["intents"].split(", "):

            print(f"   • {intent}")

# ---------------------------------------
# Export CSV
# ---------------------------------------

report = pd.DataFrame(conflicts)

report.to_csv(
    "dataset_conflicts.csv",
    index=False
)

print("\n" + "=" * 70)
print("Conflict report saved as dataset_conflicts.csv")
print("=" * 70)