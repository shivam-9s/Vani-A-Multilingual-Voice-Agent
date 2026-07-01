from src.assistant.response_templates import (
    RESPONSES,
    DEFAULT_RESPONSE
)


class ResponseGenerator:
    """
    Generates responses using centralized response templates.
    """

    def __init__(self):
        self.responses = RESPONSES

    # ======================================================
    # Main Function
    # ======================================================

    def generate(self, intent, entities):

        template = self.responses.get(intent)

        if template is None:
            return DEFAULT_RESPONSE

        # --------------------------------------------
        # Intents requiring Order ID
        # --------------------------------------------

        if "success" in template:

            if "order_id" not in entities:
                return template["missing"]

            return template["success"].format(
                order_id=entities["order_id"]
            )

        # --------------------------------------------
        # Default Response
        # --------------------------------------------

        return template.get(
            "default",
            DEFAULT_RESPONSE
        )


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    generator = ResponseGenerator()

    tests = [

        (
            "track_shipment",
            {
                "order_id": "ORD12345"
            }
        ),

        (
            "track_shipment",
            {}
        ),

        (
            "order_status",
            {
                "order_id": "ORD98765"
            }
        ),

        (
            "change_email",
            {
                "email": "abc@gmail.com"
            }
        ),

        (
            "refund_status",
            {}
        ),

        (
            "product_information",
            {}
        ),

        (
            "store_location",
            {}
        ),

        (
            "technical_support",
            {}
        ),

        (
            "unknown_intent",
            {}
        )

    ]

    print("=" * 60)
    print("VANI RESPONSE GENERATOR")
    print("=" * 60)

    for intent, entities in tests:

        print(f"\nIntent : {intent}")

        print(
            generator.generate(
                intent,
                entities
            )
        )