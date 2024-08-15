def find_largest_and_smallest():
    largest = None
    smallest = None

    while True:
        snum = input("Enter number: ")

        if snum.lower() == 'done':
            break

        try:
            number = int(snum)
        except ValueError:
            print("Invalid input")
            continue

        if largest is None or number > largest:
            largest = number

        if smallest is None or number < smallest:
            smallest = number

    if largest is not None and smallest is not None:
        print("Maximum:", largest)
        print("Minimum:", smallest)

# Run the function
find_largest_and_smallest()