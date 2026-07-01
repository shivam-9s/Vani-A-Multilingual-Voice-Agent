import os
import joblib
import pandas as pd

from datasets import Dataset
from transformers import AutoTokenizer
from sklearn.preprocessing import LabelEncoder

from src.models.config import (
    MODEL_NAME,
    TRAIN_FILE,
    TEST_FILE,
    MAX_LENGTH,
    LABEL_ENCODER
)

# =====================================================
# Load Tokenizer
# =====================================================

print("=" * 60)
print("Loading Tokenizer")
print("=" * 60)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

# =====================================================
# Load Train/Test CSV
# =====================================================

train_df = pd.read_csv(TRAIN_FILE)
test_df = pd.read_csv(TEST_FILE)

print(f"\nTraining Samples : {len(train_df)}")
print(f"Testing Samples  : {len(test_df)}")

# =====================================================
# Encode Labels
# =====================================================

label_encoder = LabelEncoder()

train_df["label"] = label_encoder.fit_transform(
    train_df["intent"]
)

test_df["label"] = label_encoder.transform(
    test_df["intent"]
)

NUM_LABELS = len(label_encoder.classes_)

# =====================================================
# Save Label Encoder
# =====================================================

os.makedirs(
    os.path.dirname(LABEL_ENCODER),
    exist_ok=True
)

joblib.dump(
    label_encoder,
    LABEL_ENCODER
)

print("\n✅ Label Encoder Saved")

# =====================================================
# Tokenization
# =====================================================

def tokenize(batch):

    return tokenizer(

        batch["text"],

        truncation=True,

        max_length=MAX_LENGTH

    )

# =====================================================
# Convert to HF Dataset
# =====================================================

train_dataset = Dataset.from_pandas(train_df)

test_dataset = Dataset.from_pandas(test_df)

# =====================================================
# Tokenize
# =====================================================

train_dataset = train_dataset.map(
    tokenize,
    batched=True
)

test_dataset = test_dataset.map(
    tokenize,
    batched=True
)

# =====================================================
# Torch Format
# =====================================================

columns = [

    "input_ids",

    "attention_mask",

    "label"

]

train_dataset.set_format(

    type="torch",

    columns=columns

)

test_dataset.set_format(

    type="torch",

    columns=columns
)

print("\nDataset Loader Ready.")

print(f"Number of Labels : {NUM_LABELS}")

print("=" * 60)