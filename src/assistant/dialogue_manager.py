class DialogueManager:
    """
    Maintains the conversation state.

    Responsibilities
    ----------------
    • Remember current intent
    • Store extracted entities
    • Maintain conversation history
    • Handle slot filling
    • Clear completed conversations
    """

    def __init__(self):
        self.reset()

    # =====================================================
    # Reset Conversation
    # =====================================================

    def reset(self):

        self.current_intent = None

        self.entities = {}

        self.history = []

        self.awaiting_input = False

        self.pending_entity = None

    # =====================================================
    # Intent
    # =====================================================

    def set_intent(self, intent):

        self.current_intent = intent

    # =====================================================
    # Entity Handling
    # =====================================================

    def update_entities(self, entities):

        self.entities.update(entities)

    # =====================================================
    # Slot Filling
    # =====================================================

    def request_entity(self, entity_name):

        self.awaiting_input = True

        self.pending_entity = entity_name

    def fill_pending_entity(self, value):

        if not self.awaiting_input:
            return

        self.entities[self.pending_entity] = value

        self.awaiting_input = False

        self.pending_entity = None

    # =====================================================
    # History
    # =====================================================

    def add_message(self, speaker, message):

        self.history.append({

            "speaker": speaker,

            "message": message

        })

    # =====================================================
    # Get State
    # =====================================================

    def get_state(self):

        return {

            "intent": self.current_intent,

            "entities": self.entities,

            "awaiting_input": self.awaiting_input,

            "pending_entity": self.pending_entity,

            "history": self.history

        }

    # =====================================================
    # Print State
    # =====================================================

    def print_state(self):

        print("\nConversation State")

        print("-" * 60)

        print("Intent :", self.current_intent)

        print("\nEntities")

        if self.entities:

            for k, v in self.entities.items():

                print(f"{k:<15}: {v}")

        else:

            print("None")

        print("\nAwaiting Input :", self.awaiting_input)

        print("Pending Entity :", self.pending_entity)

        print("\nHistory")

        if self.history:

            for msg in self.history:

                print(f"{msg['speaker']}: {msg['message']}")

        else:

            print("No conversation yet.")

    # =====================================================
    # Clear Stored Entities
    # =====================================================

    def clear_entities(self):
        """
        Remove all stored entities.
        """

        self.entities.clear()

    # =====================================================
    # Complete Conversation
    # =====================================================

    def complete_conversation(self):
        """
        Clears the current task but
        keeps conversation history.
        """

        self.current_intent = None

        self.entities.clear()

        self.awaiting_input = False

        self.pending_entity = None

    # =====================================================
    # Start New Conversation
    # =====================================================

    def start_new_conversation(self):
        """
        Alias for complete_conversation().
        """

        self.complete_conversation()


# =========================================================
# Testing
# =========================================================

if __name__ == "__main__":

    dm = DialogueManager()

    dm.set_intent("track_shipment")

    dm.request_entity("order_id")

    dm.add_message("User", "Track my order")

    dm.add_message("Bot", "Please provide your Order ID.")

    print("\nBefore Slot Filling")

    dm.print_state()

    dm.fill_pending_entity("ORD12345")

    dm.add_message("User", "ORD12345")

    print("\nAfter Slot Filling")

    dm.print_state()

    print("\nCompleting Conversation...")

    dm.complete_conversation()

    dm.print_state()