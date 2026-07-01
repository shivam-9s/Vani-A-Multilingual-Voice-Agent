import time
import torch
import joblib

from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification
)

from src.models.config import (
    OUTPUT_DIR,
    LABEL_ENCODER,
    MAX_LENGTH,
    TOP_K
)

# =========================================================
# Load Everything Once
# =========================================================

print("=" * 60)
print("Loading VANI Inference Engine...")
print("=" * 60)

tokenizer = AutoTokenizer.from_pretrained(
    OUTPUT_DIR
)

model = AutoModelForSequenceClassification.from_pretrained(
    OUTPUT_DIR
)

label_encoder = joblib.load(
    LABEL_ENCODER
)

model.eval()

print("Inference Engine Ready.\n")

# =========================================================
# Prediction Function
# =========================================================

def predict(text):

    start = time.time()

    inputs = tokenizer(

        text,

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

    top_probs, top_ids = torch.topk(
        probabilities,
        TOP_K
    )

    predictions = []

    for prob, idx in zip(top_probs, top_ids):

        intent = label_encoder.inverse_transform(
            [idx.item()]
        )[0]

        predictions.append({

            "intent": intent,

            "confidence": round(
                prob.item() * 100,
                2
            )

        })

    end = time.time()

    return {

        "input": text,

        "prediction": predictions[0],

        "top_predictions": predictions,

        "inference_time_ms": round(
            (end-start)*1000,
            2
        )

    }