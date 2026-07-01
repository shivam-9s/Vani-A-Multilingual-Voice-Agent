import os
import pandas as pd

# ==========================================================
# Configuration
# ==========================================================

INPUT_DATASET = "datasets/cleaned/training_data_clean.csv"

OUTPUT_REPORT = "datasets/reports/dataset_balance_report.csv"

TARGET_SAMPLES = 100

INTENT_COLUMN = "intent"


def main():

    print("=" * 70)
    print("VANI DATASET BALANCER")
    print("=" * 70)

    df = pd.read_csv(INPUT_DATASET)

    print(f"\nDataset Loaded : {INPUT_DATASET}")
    print(f"Samples : {len(df)}")

    counts = (
        df[INTENT_COLUMN]
        .value_counts()
        .sort_index()
    )

    rows = []

    for intent, current in counts.items():

        need = max(TARGET_SAMPLES - current, 0)

        status = (
            "Complete"
            if need == 0
            else "Needs More Samples"
        )

        rows.append({

            "intent": intent,
            "current": current,
            "target": TARGET_SAMPLES,
            "need": need,
            "status": status

        })

    report = pd.DataFrame(rows)

    os.makedirs("datasets/reports", exist_ok=True)

    report.to_csv(

        OUTPUT_REPORT,

        index=False

    )

    print("\nBalance Report Saved")

    print(OUTPUT_REPORT)

    print("\nIntent Balance\n")

    print(report.to_string(index=False))

    print("\nSummary")

    print(f"\nTotal Intents : {len(report)}")

    completed = (report["need"] == 0).sum()

    remaining = len(report) - completed

    print(f"Balanced Intents : {completed}")
    print(f"Need Improvement : {remaining}")

    total_needed = report["need"].sum()

    print(f"Samples Needed : {total_needed}")

    print("\nDataset Balance Analysis Completed.")


if __name__ == "__main__":

    main()