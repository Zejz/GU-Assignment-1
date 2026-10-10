"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""

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

    """"Choice 1"""


    if Choice == "1":
        print("Console closed. Dispatch data remains safe.")
        Running = 0


    """"Choice 2"""


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
    
    if Choice == "2":
        reference = input("Booking reference: ")
        reference = reference.upper()
        if validate_reference(reference):
            print(f"Valid reference:{reference}")
        else:
            print("Invalid booking reference")


    """Choice 3"""


    def get_service_multiplier(service_code):
        if service_code == "S":
            return 1.00
        elif service_code == "X":
            return 1.25
        else:  # "P"
            return 1.60

    def calculate_quote(distance, weight, service_code):
        subtotal = 45.00 + distance * 6.50 + weight * 4.00
        return subtotal * get_service_multiplier(service_code)

    def read_positive_number(prompt):
        while True:
            text = input(prompt)
            try:
                value = float(text)
            except ValueError:
                print("Error - Value must be a valid number.")
            else:
                if value > 0:
                    return value
                print("Error - Value must be greater than zero.")

    def read_service_code(prompt):
        while True:
            code = input(prompt).strip().upper()
            if code == "S" or code == "X" or code == "P":
                return code
            print("Error - Service code must be S, X or P.")

    def quote_service():
        distance = read_positive_number("Distance (km): ")
        weight = read_positive_number("Weight (kg): ")
        service_code = read_service_code("Service code: ")
        quote = calculate_quote(distance, weight, service_code)
        print(f"Delivery quote: {quote:.2f} SEK")

    if Choice == "3":
        quote_service()


    """Choice 4"""


    def consolidate_labels(scanned_text):
        unique_labels = []
        for item in scanned_text.split(","):
            label = item.strip().upper()
            if label not in unique_labels:
                unique_labels.append(label)
        return unique_labels


    def print_label_list(labels):
        print("Unique load list:")
        number = 1
        for label in labels:
            print(f"{number}. {label}")
            number += 1
        print(f"Total unique parcels: {len(labels)}")


    def labels_service():
        scanned_text = input("Scanned labels: ")
        labels = consolidate_labels(scanned_text)
        print_label_list(labels)


    if Choice == "4":
        labels_service()

pass


if __name__ == "__main__":
    main()
