"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""
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



def main():
    """Run the HarborFlow Dispatch Console."""

Running = 1
while Running:
    Choice = input("""HARBORFLOW DISPATCH CONSOLE
    1. Close console
    2. Validate booking reference
    3. Calculate delivery quote
    4. Consolidate parcel labels
    5. Check van capacity
    6. Classify service performance
    7. Produce weekly dispatch report
Select service: """)

    if Choice == "1":
        print("Console closed. Dispatch data remains safe.")
        Running = 0
    
    if Choice == "2":
        reference = input("Booking reference: ")
        reference = reference.upper()
        if validate_reference(reference):
            print(f"Valid reference:{reference}")
        else:
            print("Invalid booking reference")

    pass


if __name__ == "__main__":
    main()
