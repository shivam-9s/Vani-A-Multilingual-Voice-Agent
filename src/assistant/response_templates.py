"""
==========================================================
VANI RESPONSE TEMPLATES
==========================================================

This file contains response templates for all supported
intents.

The Response Generator simply looks up the intent here
instead of hardcoding responses.

==========================================================
"""

RESPONSES = {

    # ======================================================
    # Order
    # ======================================================

    "order_status": {
        "missing": "Please share your Order ID.",
        "success": "Your order {order_id} has been confirmed."
    },

    "track_shipment": {
        "missing": "Please provide your Order ID.",
        "success": "Your shipment for order {order_id} is currently in transit."
    },

    "order_confirmation": {
        "default": "Your order has been confirmed successfully."
    },

    "cancel_order": {
        "default": "Your order cancellation request has been submitted."
    },

    "modify_order": {
        "default": "Please tell me what changes you want to make to your order."
    },

    "return_order": {
        "default": "Your return request has been initiated."
    },

    "exchange_order": {
        "default": "Please tell me which product you want to exchange."
    },

    "order_history": {
        "default": "Fetching your previous orders."
    },

    "order_not_received": {
        "default": "Sorry to hear that. Let me check your delivery status."
    },

    "reorder_product": {
        "default": "Sure. I'll help you reorder the product."
    },

    # ======================================================
    # Delivery
    # ======================================================

    "delivery_status": {
        "default": "Your delivery is currently on schedule."
    },

    "delivery_delay": {
        "default": "We apologize. Your delivery has been delayed."
    },

    "delivery_agent_contact": {
        "default": "I'll share the delivery agent details shortly."
    },

    "delivery_instructions": {
        "default": "Please tell me the delivery instructions."
    },

    "change_delivery_slot": {
        "default": "Please select your preferred delivery slot."
    },

    "reschedule_delivery": {
        "default": "Your delivery can be rescheduled."
    },

    "missing_package": {
        "default": "We are investigating your missing package."
    },

    "damaged_package": {
        "default": "We're sorry. We'll help replace the damaged package."
    },

    "wrong_delivery": {
        "default": "We'll arrange pickup and send the correct item."
    },

    # ======================================================
    # Refund & Payment
    # ======================================================

    "refund_status": {
        "default": "Your refund request is currently being processed."
    },

    "refund_request": {
        "default": "Your refund request has been registered."
    },

    "payment_status": {
        "default": "Your payment has been received successfully."
    },

    "payment_failed": {
        "default": "Your payment failed. Please try again."
    },

    "payment_method_change": {
        "default": "You can update your payment method."
    },

    "duplicate_payment": {
        "default": "We are checking your duplicate payment."
    },

    "cashback_query": {
        "default": "Your cashback details are being retrieved."
    },

    "wallet_balance": {
        "default": "Fetching your wallet balance."
    },

    "promo_code_issue": {
        "default": "Please share your promo code."
    },

    # ======================================================
    # Account
    # ======================================================

    "login_issue": {
        "default": "Please tell me the login issue you're facing."
    },

    "reset_password": {
        "default": "A password reset link has been sent to your registered email."
    },

    "account_locked": {
        "default": "Your account appears to be locked."
    },

    "account_verification": {
        "default": "Let's verify your account."
    },

    "profile_update": {
        "default": "Which profile information would you like to update?"
    },

    "change_email": {
        "default": "Please provide your new email address."
    },

    "change_phone": {
        "default": "Please provide your new phone number."
    },

    "update_address": {
        "default": "Please provide your new delivery address."
    },

    "delete_account": {
        "default": "We're sorry to see you go. Please confirm account deletion."
    },

    "deactivate_account": {
        "default": "Your account can be temporarily deactivated."
    },

    "reactivate_account": {
        "default": "Your account can now be reactivated."
    },

    # ======================================================
    # Product
    # ======================================================

    "product_information": {
        "default": "Which product would you like information about?"
    },

    "product_availability": {
        "default": "Checking product availability."
    },

    "product_recommendation": {
        "default": "I'd be happy to recommend some products."
    },

    "warranty_claim": {
        "default": "Let's start your warranty claim."
    },

    "technical_support": {
        "default": "Please describe the technical issue."
    },

    # ======================================================
    # Misc
    # ======================================================

    "invoice_request": {
        "default": "I'll help you download your invoice."
    },

    "store_location": {
        "default": "Please share your city so I can find the nearest store."
    },

    "complaint_status": {
        "default": "Checking your complaint status."
    },

    "raise_complaint": {
        "default": "Please describe your issue."
    },

    "speak_to_agent": {
        "default": "Connecting you to a customer support agent."
    },

    "general_query": {
        "default": "How may I assist you today?"
    }

}


DEFAULT_RESPONSE = (
    "I'm sorry, I couldn't understand your request."
)