"""HarborFlow Assignment 1 starter file.

Replace the TODO sections with your team's implementation. Keep the program
entry point so the file can be run with: python harborflow_app.py
"""

from email.mime import text


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
    8. Compare delivery scenarios
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


    """Choice 5"""

    
    def parse_weights(text):
        """Convert a comma-separated string into a list of floats.
        Returns an empty list if invalid or non-positive.
        """
        weights = []
        for item in text.split(","):
            try:
                weight = float(item.strip())
            except ValueError:
                return []
            if weight <= 0:
                return []
            weights.append(weight)
        return weights

    def read_weights(prompt):
        """Keep asking until valid weights are provided."""
        while True:
            weights = parse_weights(input(prompt))
            if len(weights) > 0:
                return weights
            print("Error - Value must be greater than zero.")

    def check_van_capacity(capacity, weights):
        """Evaluate parcels left to right against van capacity."""
        decisions = []
        accepted = 0
        loaded = 0.0
        for weight in weights:
            if loaded + weight <= capacity:
                decisions.append(True)
                accepted += 1
                loaded += weight
            else:
                decisions.append(False)
        return decisions, accepted, loaded

    def print_capacity_report(capacity, decisions, accepted, loaded):
        """Print the decision for each parcel and the final summary."""
        for i, decision in enumerate(decisions, start=1):
            status = "ACCEPTED" if decision else "REJECTED"
            print(f"Parcel {i}: {status}")
        print(f"Accepted parcels: {accepted}")
        print(f"Loaded weight: {loaded:.2f} kg")
        print(f"Remaining capacity: {capacity - loaded:.2f} kg")

    def capacity_service():
        """Task 5: read capacity and weights, then print report."""
        capacity = read_positive_number("Van capacity (kg): ")
        weights = read_weights("Parcel weights (kg): ")
        decisions, accepted, loaded = check_van_capacity(capacity, weights)
        print_capacity_report(capacity, decisions, accepted, loaded)

    if Choice == "5":
        capacity_service()


    """Choice 6"""


    def read_non_negative_int(prompt):
        """Prompt until a non-negative integer is entered."""
        while True:
            try:
                value = int(input(prompt))
                if value >= 0:
                    return value
            except ValueError:
                pass
            print("Error - Value must be greater than zero.")

    def classify_performance(promised, actual, damaged):
        """Determine delay and service status."""
        delay = actual - promised
        if damaged > 0:
            status = "SERVICE FAILURE"
        elif delay <= 0:
            status = "ON TIME"
        elif delay <= 15:
            status = "MINOR DELAY"
        else:
            status = "MAJOR DELAY"
        return delay, status

    def performance_service():
        """Task 6: read route figures, print delay and status."""
        promised = read_non_negative_int("Promised minutes: ")
        actual = read_non_negative_int("Actual minutes: ")
        damaged = read_non_negative_int("Damaged parcels: ")
        delay, status = classify_performance(promised, actual, damaged)
        print(f"Delay: {delay} minutes")
        print(f"Service status: {status}")

    if Choice == "6":
        performance_service()

    
    """Choice 7"""


    def read_completed_deliveries(prompt):
        """Prompt for and read completed deliveries."""
        while True:
            try:
                values = input(prompt).split(",")
                if len(values) != 7:
                    print("Error - Weekly report requires 7 delivery counts.")
                    continue
                deliveries = [int(x) for x in values]
                if any(delivery <= 0 for delivery in deliveries):
                    print("Error - All delivery values must be positive integers.")
                    continue
                return deliveries
            except ValueError:
                print("Error - Please enter valid integers.")

    def calculate_total_deliveries(completed):
        total = 0
        for delivery in completed:
            total += delivery
        return total

    def calculate_total_deliveries(completed):
        total = 0
        for delivery in completed:
            total += delivery
        return total

    def calculate_average(total_deliveries):
        average = total_deliveries / 7
        return average

    def calculate_highest(completed):
        highest = None
        highest_day = None
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        position = 0
        for delivery in completed:
            if highest is None or delivery > highest:
                highest = delivery
                highest_day = weekdays[position]
            position += 1
        return highest, highest_day

    def calculate_lowest(completed):
        lowest = None
        lowest_day = None
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        position = 0
        for delivery in completed:
            if lowest is None or delivery < lowest:
                lowest = delivery
                lowest_day = weekdays[position]
            position += 1
        return lowest, lowest_day

    def calculate_target_days(completed, daily_target):
        target_days = 0
        for delivery in completed:
            if delivery >= daily_target:
                target_days += 1
        return target_days

    def dispatch_report():
        completed = read_completed_deliveries("Completed deliveries: ")
        daily_target = int(input("Weekly target: ")) / 7
        print("Weekly dispatch report")
        total = calculate_total_deliveries(completed)
        print(f"Total deliveries: {total}")
        average = calculate_average(total)
        print(f"Average per daily: {average:.2f}")
        highest, highest_day = calculate_highest(completed)
        print(f"Highest day: {highest_day} ({highest})")
        lowest, lowest_day = calculate_lowest(completed)
        print(f"Lowest day: {lowest_day} ({lowest})")
        target_days = calculate_target_days(completed, daily_target)
        print(f"Days meeting target: {target_days}")

    if Choice == "7":
        dispatch_report()


    """Choice 8"""


    def quote_service():
            distance = read_positive_number("Distance (km): ")
            weight = read_positive_number("Weight (kg): ")
            service_code = "S"
            quote_S = calculate_quote(distance, weight, service_code)
            service_code = "X"
            quote_X = calculate_quote(distance, weight, service_code)
            service_code = "P"
            quote_P = calculate_quote(distance, weight, service_code)
            print("Service comparison")
            print(f"Standard: {quote_S:.2f} SEK")
            print(f"Express: {quote_X:.2f} SEK")
            print(f"Priority: {quote_P:.2f} SEK")

            print("Cheapest service: ", end="")
            if quote_S <= quote_X and quote_S <= quote_P:
                print("Standard")
            elif quote_X <= quote_P:
                print("Express")
            else:
                print("Priority")

            print("Most expensive service: ", end="")
            if quote_S >= quote_X and quote_S >= quote_P:
                print("Standard")
            elif quote_X >= quote_P:
                print("Express")
            else:
                print("Priority")

    if Choice == "8":
        quote_service()



    else:
        print("Error - Select a service from 1 to 8.")
        
pass


if __name__ == "__main__":
    main()
