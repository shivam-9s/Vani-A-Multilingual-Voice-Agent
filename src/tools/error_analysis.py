import os
import joblib
import torch
import pandas as pd

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

from src.models.config import (
    TEST_FILE,
    OUTPUT_DIR,
    LABEL_ENCODER,
    REPORT_FOLDER,
    MAX_LENGTH
)

# ==========================================================
# Create Reports Folder
# ==========================================================

os.makedirs(REPORT_FOLDER, exist_ok=True)

# ==========================================================
# Load Model
# ==========================================================

print("=" * 60)
print("VANI ERROR ANALYSIS")
print("=" * 60)

tokenizer = AutoTokenizer.from_pretrained(OUTPUT_DIR)

model = AutoModelForSequenceClassification.from_pretrained(
    OUTPUT_DIR
)

model.eval()

label_encoder = joblib.load(LABEL_ENCODER)

# ==========================================================
# Load Test Dataset
# ==========================================================

df = pd.read_csv(TEST_FILE)

results = []

correct = 0

# ==========================================================
# Prediction Loop
# ==========================================================

for _, row in df.iterrows():

    sentence = row["text"]

    actual = row["intent"]

    inputs = tokenizer(

        sentence,

        return_tensors="pt",

        truncation=True,

        max_length=MAX_LENGTH

    )

    with torch.no_grad():

        outputs = model(**inputs)

        probabilities = torch.softmax(
            outputs.logits,
            dim=1
        )[0]

    confidence, prediction = torch.max(
        probabilities,
        dim=0
    )

    predicted = label_encoder.inverse_transform(
        [prediction.item()]
    )[0]

    is_correct = predicted == actual

    if is_correct:
        correct += 1

    results.append({

        "sentence": sentence,

        "actual_intent": actual,

        "predicted_intent": predicted,

        "confidence": round(
            confidence.item() * 100,
            2
        ),

        "correct": is_correct

    })

# ==========================================================
# Save Report
# ==========================================================

report = pd.DataFrame(results)

report.to_csv(

    os.path.join(
        REPORT_FOLDER,
        "error_analysis.csv"
    ),

    index=False

)

# ==========================================================
# Statistics
# ==========================================================

accuracy = correct / len(df)

print()

print(f"Total Samples : {len(df)}")

print(f"Correct       : {correct}")

print(f"Wrong         : {len(df)-correct}")

print(f"Accuracy      : {accuracy*100:.2f}%")

print()

print("Saved Report:")

print(

    os.path.join(
        REPORT_FOLDER,
        "error_analysis.csv"
    )

)

print("=" * 60)