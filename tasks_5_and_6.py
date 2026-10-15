# ---------------------------------------------------------------- Task 5 ---

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


# ---------------------------------------------------------------- Task 6 ---

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