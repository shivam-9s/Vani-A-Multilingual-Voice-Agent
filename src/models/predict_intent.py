from src.inference.predictor import predict

print("=" * 60)
print("VANI MULTILINGUAL ASSISTANT")
print("=" * 60)

while True:

    sentence = input(
        "\nEnter Sentence (exit to quit): "
    ).strip()

    if sentence.lower() == "exit":
        break

    if len(sentence) == 0:
        print("Please enter a sentence.")
        continue

    result = predict(sentence)

    print("\n" + "="*60)

    print("INPUT")

    print(result["input"])

    print("\nTOP PREDICTIONS")

    for i, item in enumerate(

        result["top_predictions"],

        start=1

    ):

        print(

            f"{i}. "

            f"{item['intent']:<30}"

            f"{item['confidence']:.2f}%"

        )

    print("\nFINAL PREDICTION")

    print(

        result["prediction"]["intent"]

    )

    print(

        f"\nConfidence : "

        f"{result['prediction']['confidence']:.2f}%"

    )

    print(

        f"Inference Time : "

        f"{result['inference_time_ms']} ms"

    )

    print("="*60)