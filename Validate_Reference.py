def validate_reference(reference):
    """Validate a booking reference.

    A valid booking reference is a string of 12 characters, where the first
    three characters are HFL, and the next character is a dash followed by a three letter sequence
    followed by a dash and then a four digit number. For example, HFL-CCC-1234 is a valid booking reference.

    Args:
        reference (str): The booking reference to validate.

    Returns:
        bool: True if the booking reference is valid, False otherwise.
    """
    reference = reference.upper()

    if len(reference) != 12:
        return False
    if not reference.startswith("HFL"):
        return False
    if reference[3] != "-":
        return False
    if not reference[4:7].isalpha() or not reference[4:7].isupper():
        return False
    if reference[7] != "-":
        return False
    if not reference[8:].isdigit():
        return False
    return True
