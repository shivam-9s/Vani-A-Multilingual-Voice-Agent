import re


class EntityExtractor:
    """
    Extracts useful entities from user text.

    Current Supported Entities
    --------------------------
    • order_id
    • email
    • phone
    • pincode
    • date
    • quantity
    """

    def __init__(self):

        self.date_keywords = [
            "today",
            "tomorrow",
            "yesterday",
            "monday",
            "tuesday",
            "wednesday",
            "thursday",
            "friday",
            "saturday",
            "sunday",
        ]

    # ======================================================
    # Main Extraction Function
    # ======================================================

    def extract(self, text: str):

        entities = {}

        # ------------------------------------------
        # Order ID
        # ------------------------------------------

        order = re.search(
            r"\b(?:ORD|ORDER)[-_]?\d+\b",
            text,
            re.IGNORECASE,
        )

        if order:
            entities["order_id"] = order.group()

        # ------------------------------------------
        # Email
        # ------------------------------------------

        email = re.search(
            r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
            text,
        )

        if email:
            entities["email"] = email.group()

        # ------------------------------------------
        # Phone Number
        # ------------------------------------------

        phone = re.search(
            r"\b[6-9]\d{9}\b",
            text,
        )

        if phone:
            entities["phone"] = phone.group()

        # ------------------------------------------
        # Indian Pincode
        # ------------------------------------------

        pincode = re.search(
            r"\b\d{6}\b",
            text,
        )

        if pincode:
            entities["pincode"] = pincode.group()

        # ------------------------------------------
        # Date Keywords
        # ------------------------------------------

        lower_text = text.lower()

        for keyword in self.date_keywords:

            if keyword in lower_text:
                entities["date"] = keyword
                break

        # ------------------------------------------
        # Quantity
        # ------------------------------------------

        # Quantity should NOT be extracted
        # if the detected number is actually
        # a phone number, pincode or order id.

        quantity = None

        if (
            "phone" not in entities
            and "pincode" not in entities
            and "order_id" not in entities
        ):

            qty = re.search(r"\b\d+\b", text)

            if qty:
                quantity = qty.group()

        if quantity:
            entities["quantity"] = quantity

        return entities


# ==========================================================
# Testing
# ==========================================================

if __name__ == "__main__":

    extractor = EntityExtractor()

    print("=" * 60)
    print("VANI ENTITY EXTRACTOR")
    print("=" * 60)

    while True:

        sentence = input("\nEnter Text (type exit to quit): ")

        if sentence.lower() == "exit":
            break

        entities = extractor.extract(sentence)

        print("\nExtracted Entities")

        if entities:

            for key, value in entities.items():
                print(f"{key:<12}: {value}")

        else:

            print("No entities found.")