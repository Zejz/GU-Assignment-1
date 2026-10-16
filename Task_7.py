def Completed_deliveries(deliveries):
    """
    Return the deliveries when given exactly seven positive integers.
    """
    if not isinstance(deliveries, list) or len(deliveries) != 7:
        return "Error: deliveries must be a list of exactly 7 integers."
    if any(type(delivery) is not int for delivery in deliveries):
        return "Error: deliveries must be a list of exactly 7 integers."

    completed = []
    for delivered in deliveries:
        if delivered <= 0:
            return []
        completed.append(delivered)
    return completed


def calculate_daily_target(int):
    daily_target = int / 7
    return daily_target


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
    completed = Completed_deliveries("Completed deliveries: ")
    daily_target = calculate_daily_target("Weekly target: ")
    print("Weekly dispatch report")
    total = calculate_total_deliveries(completed)
    print(f"Total deliveries: {total}")
    average = calculate_average(total)
    print(f"Average per daily: {average}")
    highest, highest_day = calculate_highest(completed)
    print(f"Highest day: {highest_day} ({highest})")
    lowest, lowest_day = calculate_lowest(completed)
    print(f"Lowest day: {lowest_day} ({lowest})")
    target_days = calculate_target_days(completed, daily_target)
    print(f"Days meeting target: {target_days}")