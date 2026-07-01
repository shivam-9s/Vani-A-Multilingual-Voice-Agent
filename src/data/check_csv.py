import csv

file_path = "datasets/raw/training_data.csv"

with open(file_path, "r", encoding="utf-8") as file:
    reader = csv.reader(file)

    print("Checking CSV file...\n")

    for line_number, row in enumerate(reader, start=1):
        if len(row) != 2:
            print(f"❌ Line {line_number}: Found {len(row)} columns")
            print(row)
            print("-" * 60)

print("\nFinished checking.")