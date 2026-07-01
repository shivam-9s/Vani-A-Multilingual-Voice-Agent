"""
VANI INPUT VALIDATOR
"""

INVALID_INPUTS = {
    "",
    "you",
    "you:",
    "bot",
    "bot:",
    "assistant",
    "assistant:",
}


def is_valid(text: str) -> bool:
    """
    Returns True if the input should be processed.
    """

    if text is None:
        return False

    text = text.strip().lower()

    if text in INVALID_INPUTS:
        return False

    if len(text) == 0:
        return False

    return True