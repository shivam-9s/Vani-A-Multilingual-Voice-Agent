import numpy as np

from evaluate import load

# -------------------------------
# Load Evaluation Metrics
# -------------------------------

accuracy_metric = load("accuracy")
precision_metric = load("precision")
recall_metric = load("recall")
f1_metric = load("f1")


def compute_metrics(eval_pred):
    """
    Computes evaluation metrics for the intent classifier.
    """

    logits, labels = eval_pred

    predictions = np.argmax(logits, axis=1)

    accuracy = accuracy_metric.compute(
        predictions=predictions,
        references=labels
    )["accuracy"]

    precision = precision_metric.compute(
        predictions=predictions,
        references=labels,
        average="weighted"
    )["precision"]

    recall = recall_metric.compute(
        predictions=predictions,
        references=labels,
        average="weighted"
    )["recall"]

    f1 = f1_metric.compute(
        predictions=predictions,
        references=labels,
        average="weighted"
    )["f1"]

    return {
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1
    }