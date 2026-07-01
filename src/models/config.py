# ==========================================================
# VANI - Project Configuration
# ==========================================================

# -------------------------------
# HuggingFace Model
# -------------------------------

MODEL_NAME = "distilbert-base-multilingual-cased"

# ==========================================================
# DATASET PATHS
# ==========================================================

RAW_DATASET = "datasets/raw/training_data.csv"

CLEAN_DATASET = "datasets/raw/training_data.csv"

INTENT_LIST = "datasets/intents/intent_list.csv"

TRAIN_FILE = "datasets/processed/train.csv"

TEST_FILE = "datasets/processed/test.csv"

REPORT_FOLDER = "datasets/reports"

# ==========================================================
# MODEL PATHS
# ==========================================================

OUTPUT_DIR = "models/intent_classifier"

LABEL_ENCODER = "models/intent_classifier/label_encoder.pkl"

# ==========================================================
# TRAINING PARAMETERS
# ==========================================================

MAX_LENGTH = 160

BATCH_SIZE = 16

EPOCHS = 10

LEARNING_RATE = 1e-5

RANDOM_SEED = 42

# ==========================================================
# PREDICTION SETTINGS
# ==========================================================

TOP_K = 5

HIGH_CONFIDENCE = 80

MEDIUM_CONFIDENCE = 50