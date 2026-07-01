import os
import joblib
import torch
import numpy as np
import matplotlib.pyplot as plt

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    ConfusionMatrixDisplay
)

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

from src.models.config import TEST_FILE
import pandas as pd

# ------------------------------------
# Load Model
# ------------------------------------

MODEL_PATH = "models/intent_classifier"

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)

model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

model.eval()

# ------------------------------------
# Load Label Encoder
# ------------------------------------

label_encoder = joblib.load(
    os.path.join(MODEL_PATH, "label_encoder.pkl")
)

# ------------------------------------
# Load Test Dataset
# ------------------------------------

df = pd.read_csv(TEST_FILE)

texts = df["text"].tolist()

true_labels = df["intent"].tolist()

predictions = []

# ------------------------------------
# Predict
# ------------------------------------

print("Predicting test samples...")

for text in texts:

    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=128
    )

    with torch.no_grad():

        outputs = model(**inputs)

        pred = torch.argmax(outputs.logits, dim=1).item()

    predictions.append(
        label_encoder.inverse_transform([pred])[0]
    )

# ------------------------------------
# Classification Report
# ------------------------------------

print("\n")
print("=" * 70)
print("CLASSIFICATION REPORT")
print("=" * 70)

print(

    classification_report(

        true_labels,

        predictions,

        digits=4,

        zero_division=0

    )

)

# ------------------------------------
# Confusion Matrix
# ------------------------------------

labels = label_encoder.classes_

cm = confusion_matrix(

    true_labels,

    predictions,

    labels=labels

)

fig, ax = plt.subplots(figsize=(22,22))

disp = ConfusionMatrixDisplay(

    confusion_matrix=cm,

    display_labels=labels

)

disp.plot(

    xticks_rotation=90,

    cmap="Blues",

    ax=ax,

    colorbar=False

)

plt.title("Intent Classification Confusion Matrix")

plt.tight_layout()

plt.savefig("confusion_matrix.png")

print("\nConfusion Matrix saved as confusion_matrix.png")

plt.show()