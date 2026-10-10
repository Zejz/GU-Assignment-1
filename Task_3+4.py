# ---------------------------------------------------------------- Task 3 ---

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
            print("Error - Value must be greater than zero.")
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

    # ---------------------------------------------------------------- Task 4 ---

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