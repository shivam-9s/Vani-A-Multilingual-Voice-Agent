from src.inference.predictor import predict
from src.assistant.entity_extractor import EntityExtractor
from src.assistant.dialogue_manager import DialogueManager
from src.assistant.response_generator import ResponseGenerator
from src.assistant.input_validator import is_valid


# ==========================================================
# VANI ASSISTANT ENGINE
# ==========================================================

class VaniAssistant:

    def __init__(self):

        print("=" * 60)
        print("Loading VANI Assistant...")
        print("=" * 60)

        self.extractor = EntityExtractor()
        self.dialogue = DialogueManager()
        self.response_generator = ResponseGenerator()

        print("Assistant Ready.\n")

    # ======================================================
    # Main Chat Function
    # ======================================================

    def chat(self, user_text):

        # --------------------------------------------------
        # Validate Input
        # --------------------------------------------------

        if not is_valid(user_text):

            return {
                "intent": None,
                "confidence": None,
                "entities": {},
                "response": "Please enter a valid message.",
                "top_predictions": [],
                "inference_time_ms": 0
            }

        # Save User Message
        self.dialogue.add_message("User", user_text)

        # --------------------------------------------------
        # SLOT FILLING
        # --------------------------------------------------

        if self.dialogue.awaiting_input:

            entities = self.extractor.extract(user_text)

            pending = self.dialogue.pending_entity

            if pending in entities:

                self.dialogue.fill_pending_entity(
                    entities[pending]
                )

                response = self.response_generator.generate(
                    self.dialogue.current_intent,
                    self.dialogue.entities
                )

                self.dialogue.add_message("Bot", response)

                final_intent = self.dialogue.current_intent
                final_entities = self.dialogue.entities.copy()

                # Clear temporary conversation
                self.dialogue.complete_conversation()

                return {
                    "intent": final_intent,
                    "confidence": "Conversation",
                    "entities": final_entities,
                    "response": response,
                    "top_predictions": [],
                    "inference_time_ms": 0
                }

            else:

                response = (
                    f"I am still waiting for your "
                    f"{pending.replace('_', ' ')}."
                )

                self.dialogue.add_message("Bot", response)

                return {
                    "intent": self.dialogue.current_intent,
                    "confidence": "Conversation",
                    "entities": self.dialogue.entities,
                    "response": response,
                    "top_predictions": [],
                    "inference_time_ms": 0
                }

        # --------------------------------------------------
        # INTENT PREDICTION
        # --------------------------------------------------

        prediction = predict(user_text)

        intent = prediction["prediction"]["intent"]
        confidence = prediction["prediction"]["confidence"]
        top_predictions = prediction["top_predictions"]
        inference_time = prediction["inference_time_ms"]

        self.dialogue.set_intent(intent)

        # --------------------------------------------------
        # ENTITY EXTRACTION
        # --------------------------------------------------

        entities = self.extractor.extract(user_text)

        self.dialogue.update_entities(entities)

        # --------------------------------------------------
        # REQUIRED ENTITY CHECK
        # --------------------------------------------------

        required_entities = {

            "track_shipment": "order_id",

            "order_status": "order_id",

            "change_email": "email",

            "change_phone": "phone",

            "update_address": "address"

        }

        if intent in required_entities:

            needed = required_entities[intent]

            if needed not in self.dialogue.entities:

                self.dialogue.request_entity(needed)

                prompts = {

                    "order_id": "Please provide your Order ID.",

                    "email": "Please provide your email address.",

                    "phone": "Please provide your phone number.",

                    "address": "Please provide your new address."

                }

                response = prompts.get(
                    needed,
                    f"Please provide your {needed.replace('_', ' ')}."
                )

                self.dialogue.add_message("Bot", response)

                return {

                    "intent": intent,

                    "confidence": confidence,

                    "entities": self.dialogue.entities,

                    "response": response,

                    "top_predictions": top_predictions,

                    "inference_time_ms": inference_time

                }

        # --------------------------------------------------
        # GENERATE RESPONSE
        # --------------------------------------------------

        response = self.response_generator.generate(
            intent,
            self.dialogue.entities
        )

        self.dialogue.add_message("Bot", response)

        final_entities = self.dialogue.entities.copy()

        # --------------------------------------------------
        # Auto Complete Simple Conversations
        # --------------------------------------------------

        completion_intents = {

            "reset_password",

            "refund_status",

            "refund_request",

            "store_location",

            "technical_support",

            "general_query",

            "product_information",

            "product_availability",

            "product_recommendation",

            "invoice_request",

            "wallet_balance",

            "account_locked",

            "account_verification",

            "cashback_query",

            "complaint_status",

            "delivery_status",

            "delivery_delay",

            "delivery_agent_contact",

            "delivery_instructions",

            "duplicate_payment",

            "missing_package",

            "promo_code_issue",

            "raise_complaint",

            "reactivate_account",

            "deactivate_account",

            "speak_to_agent",

            "warranty_claim"

        }

        if intent in completion_intents:

            self.dialogue.complete_conversation()

        return {

            "intent": intent,

            "confidence": confidence,

            "entities": final_entities,

            "response": response,

            "top_predictions": top_predictions,

            "inference_time_ms": inference_time

        }


# ==========================================================
# Interactive Assistant
# ==========================================================

if __name__ == "__main__":

    assistant = VaniAssistant()

    print("=" * 60)
    print("VANI ASSISTANT")
    print("Type 'exit' to quit")
    print("=" * 60)

    while True:

        user = input("\nYou : ")

        if user.lower() == "exit":

            print("\nGoodbye!")
            break

        result = assistant.chat(user)

        print("\n" + "=" * 60)

        print("Intent      :", result["intent"])
        print("Confidence  :", result["confidence"])
        print("Inference   :", result["inference_time_ms"], "ms")

        print("\nEntities")

        if result["entities"]:

            for key, value in result["entities"].items():

                print(f"{key:<15}: {value}")

        else:

            print("None")

        if result["top_predictions"]:

            print("\nTop Predictions")

            for pred in result["top_predictions"]:

                print(
                    f"{pred['intent']:<30}"
                    f"{pred['confidence']}%"
                )

        print("\nVani")

        print(result["response"])

        print("=" * 60)