import os
import json

from transformers import (
    AutoModelForSequenceClassification,
    Trainer,
    TrainingArguments,
    DataCollatorWithPadding
)

from src.models.config import (
    MODEL_NAME,
    OUTPUT_DIR,
    EPOCHS,
    BATCH_SIZE,
    LEARNING_RATE,
    RANDOM_SEED
)

from src.models.dataset_loader import (
    train_dataset,
    test_dataset,
    tokenizer,
    NUM_LABELS
)

from src.models.metrics import compute_metrics

# =====================================================
# Create Output Directory
# =====================================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =====================================================
# Load Model
# =====================================================

print("=" * 60)
print("Loading Pretrained Model...")
print("=" * 60)

model = AutoModelForSequenceClassification.from_pretrained(
    MODEL_NAME,
    num_labels=NUM_LABELS
)

# =====================================================
# Data Collator
# =====================================================

data_collator = DataCollatorWithPadding(
    tokenizer=tokenizer
)

# =====================================================
# Training Arguments
# =====================================================

training_args = TrainingArguments(

    output_dir=OUTPUT_DIR,

    do_train=True,

    do_eval=True,

    eval_strategy="epoch",

    save_strategy="epoch",

    logging_strategy="steps",

    logging_steps=20,

    num_train_epochs=EPOCHS,

    learning_rate=LEARNING_RATE,

    per_device_train_batch_size=BATCH_SIZE,

    per_device_eval_batch_size=BATCH_SIZE,

    load_best_model_at_end=True,

    metric_for_best_model="accuracy",

    greater_is_better=True,

    save_total_limit=2,

    report_to="none",

    seed=RANDOM_SEED
)

# =====================================================
# Trainer
# =====================================================

trainer = Trainer(

    model=model,

    args=training_args,

    train_dataset=train_dataset,

    eval_dataset=test_dataset,

    processing_class=tokenizer,

    data_collator=data_collator,

    compute_metrics=compute_metrics

)

# =====================================================
# Train
# =====================================================

print("\n" + "=" * 60)
print("Starting Training")
print("=" * 60)

trainer.train()

# =====================================================
# Evaluate
# =====================================================

print("\n" + "=" * 60)
print("Evaluating Model")
print("=" * 60)

results = trainer.evaluate()

for key, value in results.items():
    print(f"{key:<25} : {value}")

# =====================================================
# Save Model
# =====================================================

print("\nSaving Model...")

trainer.save_model(OUTPUT_DIR)

tokenizer.save_pretrained(OUTPUT_DIR)

# =====================================================
# Save Training Metadata
# =====================================================

metadata = {

    "model_name": MODEL_NAME,

    "epochs": EPOCHS,

    "batch_size": BATCH_SIZE,

    "learning_rate": LEARNING_RATE,

    "num_labels": NUM_LABELS,

    "seed": RANDOM_SEED,

    "evaluation": results

}

with open(

    os.path.join(
        OUTPUT_DIR,
        "training_metadata.json"
    ),

    "w"

) as f:

    json.dump(
        metadata,
        f,
        indent=4
    )

print("\nTraining metadata saved.")

print("=" * 60)
print("Training Completed Successfully")
print("=" * 60)

print(f"\nModel saved to:\n{OUTPUT_DIR}")