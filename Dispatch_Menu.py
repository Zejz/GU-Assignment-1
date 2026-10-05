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
        Running = 0
