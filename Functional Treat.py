# ==========================================================
# PROJECT: FUNCTIONAL TREAT
# Data Analyzer and Transformer
# BY HARSH PRAJAPATI
# ==========================================================

# Global variable
total_values = 0


# ----------------------------------------------------------
# 1. User Defined Function
# ----------------------------------------------------------
def calculate_average(data):
    """Calculate the average of the dataset."""
    if len(data) == 0:
        return 0

    return sum(data) / len(data)


# ----------------------------------------------------------
# 2. Find Duplicate Values
# ----------------------------------------------------------
def find_duplicates(data):
    """Find duplicate values from the dataset."""

    duplicates = []

    for value in data:
        if data.count(value) > 1 and value not in duplicates:
            duplicates.append(value)

    return duplicates


# ----------------------------------------------------------
# 3. Find Unique Values
# ----------------------------------------------------------
def find_unique(data):
    """Display unique values from the dataset."""

    unique = []

    for value in data:
        if value not in unique:
            unique.append(value)

    return unique


# ----------------------------------------------------------
# 4. *args Function
# ----------------------------------------------------------
def show_values(*args):
    """Display multiple values using *args."""

    print("\nValues using *args:")

    for value in args:
        print(value)


# ----------------------------------------------------------
# 5. **kwargs Function
# ----------------------------------------------------------
def show_dataset_info(**kwargs):
    """Display dataset information using **kwargs."""

    print("\nDataset Information:")

    for key, value in kwargs.items():
        print(key, ":", value)


# ----------------------------------------------------------
# 6. Recursive Factorial Function
# ----------------------------------------------------------
def factorial(number):
    """Calculate factorial using recursion."""

    if number == 0 or number == 1:
        return 1

    return number * factorial(number - 1)


# ----------------------------------------------------------
# 7. Recursive Fibonacci Function
# ----------------------------------------------------------
def fibonacci(number):
    """Calculate Fibonacci number using recursion."""

    if number == 0:
        return 0

    if number == 1:
        return 1

    return fibonacci(number - 1) + fibonacci(number - 2)


# ----------------------------------------------------------
# 8. Lambda + Filter Function
# ----------------------------------------------------------
def filter_data(data, threshold):
    """Filter values greater than or equal to threshold."""

    result = list(filter(lambda x: x >= threshold, data))

    return result


# ----------------------------------------------------------
# 9. Lambda + Map Function
# ----------------------------------------------------------
def double_values(data):
    """Double every value using lambda and map."""

    result = list(map(lambda x: x * 2, data))

    return result


# ----------------------------------------------------------
# 10. Global Keyword
# ----------------------------------------------------------
def update_total(data):
    """Update the global total number of values."""

    global total_values

    total_values = len(data)


# ----------------------------------------------------------
# 11. Return Multiple Values
# ----------------------------------------------------------
def dataset_statistics(data):
    """Return minimum, maximum, sum and average."""

    minimum = min(data)
    maximum = max(data)
    total = sum(data)
    average = calculate_average(data)

    return minimum, maximum, total, average


# ----------------------------------------------------------
# 12. Display 2D List
# ----------------------------------------------------------
def display_2d_list(data):
    """Display a 2D list in grid format."""

    print("\n2D List:")

    for row in data:
        for value in row:
            print(value, end=" ")
        print()


# ----------------------------------------------------------
# 13. Input 1D Data
# ----------------------------------------------------------
def input_1d_data():
    """Take 1D list input from the user."""

    numbers = input("\nEnter numbers separated by spaces: ")

    data = []

    for number in numbers.split():
        data.append(int(number))

    return data


# ----------------------------------------------------------
# 14. Input 2D Data
# ----------------------------------------------------------
def input_2d_data():
    """Take 2D list input from the user."""

    rows = int(input("\nEnter number of rows: "))
    columns = int(input("Enter number of columns: "))

    data = []

    for i in range(rows):

        row = []

        print("Enter values for row", i + 1)

        for j in range(columns):
            value = int(input("Enter value: "))
            row.append(value)

        data.append(row)

    return data


# ==========================================================
# MAIN PROGRAM
# ==========================================================

print("**********************************************")
print("     WELCOME TO FUNCTIONAL TREAT")
print(" Data Analyzer and Transformer Program")
print("     CREATED BY HARSH PRAJAPATI")
print("**********************************************")


data = []

while True:

    print("\nMain Menu")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
    print("1. Input Data")
    print("2. Display Data Summary")
    print("3. Calculate Factorial / Fibonacci")
    print("4. Filter Data by Threshold")
    print("5. Sort Data")
    print("6. Display Dataset Statistics")
    print("7. Exit Program")
    print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")

    choice = input("Please enter your choice: ")


    # ======================================================
    # OPTION 1 - INPUT DATA
    # ======================================================
    if choice == "1":

        print("\nInput Data")
        print("1. Enter 1D List")
        print("2. Enter 2D List")

        data_type = input("Enter your choice: ")

        if data_type == "1":

            data = input_1d_data()

            # Update global variable
            update_total(data)

            print("\nData has been stored successfully!")

            print("Your 1D Data:", data)

        elif data_type == "2":

            data_2d = input_2d_data()

            print("\n2D Data has been stored successfully!")

            display_2d_list(data_2d)

        else:

            print("\nInvalid choice!")


    # ======================================================
    # OPTION 2 - DATA SUMMARY
    # ======================================================
    elif choice == "2":

        if len(data) == 0:

            print("\nPlease enter 1D data first.")

        else:

            print("\nData Summary")
            print("----------------------------------------------")

            # Built-in functions
            print("Total elements:", len(data))
            print("Minimum value:", min(data))
            print("Maximum value:", max(data))
            print("Sum of all values:", sum(data))

            average = calculate_average(data)

            print("Average value:", round(average, 2))

            # Unique values
            unique = find_unique(data)

            print("Unique values:", unique)

            # Duplicate values
            duplicates = find_duplicates(data)

            print("Duplicate values:", duplicates)

            # Global variable
            print("Global total values:", total_values)

            # __doc__
            print("\nFunction Documentation:")
            print(calculate_average.__doc__)

            # *args
            show_values("Python", "Functions", "Lists")

            # **kwargs
            show_dataset_info(
                Total_Elements=len(data),
                Minimum=min(data),
                Maximum=max(data),
                Average=round(average, 2)
            )

            # map()
            doubled = double_values(data)

            print("\nValues after using map() and lambda:")
            print(doubled)


    # ======================================================
    # OPTION 3 - RECURSION
    # ======================================================
    elif choice == "3":

        print("\nRecursion")
        print("1. Factorial")
        print("2. Fibonacci")

        recursion_choice = input("Enter your choice: ")

        if recursion_choice == "1":

            number = int(input("\nEnter a number: "))

            if number < 0:

                print("Factorial is not possible for negative numbers.")

            else:

                result = factorial(number)

                print("\nFactorial of", number, "is:", result)

        elif recursion_choice == "2":

            number = int(input("\nEnter Fibonacci position: "))

            if number < 0:

                print("Please enter a positive number.")

            else:

                result = fibonacci(number)

                print("\nFibonacci value at position", number, "is:", result)

        else:

            print("\nInvalid choice!")


    # ======================================================
    # OPTION 4 - FILTER DATA
    # ======================================================
    elif choice == "4":

        if len(data) == 0:

            print("\nPlease enter 1D data first.")

        else:

            threshold = int(
                input("\nEnter a threshold value: ")
            )

            filtered = filter_data(data, threshold)

            print("\nFiltered Data (values >= threshold):")

            if len(filtered) == 0:

                print("No values found.")

            else:

                print(filtered)


    # ======================================================
    # OPTION 5 - SORT DATA
    # ======================================================
    elif choice == "5":

        if len(data) == 0:

            print("\nPlease enter 1D data first.")

        else:

            print("\nChoose sorting option:")
            print("1. Ascending")
            print("2. Descending")
            print("3. Show sorted() result")

            sort_choice = input("Enter your choice: ")

            if sort_choice == "1":

                # sort() changes original list
                data.sort()

                print("\nSorted Data in Ascending Order:")
                print(data)

            elif sort_choice == "2":

                # sort() changes original list
                data.sort(reverse=True)

                print("\nSorted Data in Descending Order:")
                print(data)

            elif sort_choice == "3":

                # sorted() creates a new sorted list
                new_data = sorted(data)

                print("\nOriginal Data:")
                print(data)

                print("\nNew Sorted Data using sorted():")
                print(new_data)

            else:

                print("\nInvalid choice!")


    # ======================================================
    # OPTION 6 - MULTIPLE RETURN VALUES
    # ======================================================
    elif choice == "6":

        if len(data) == 0:

            print("\nPlease enter 1D data first.")

        else:

            minimum, maximum, total, average = dataset_statistics(data)

            print("\nDataset Statistics")
            print("----------------------------------------------")
            print("Minimum value:", minimum)
            print("Maximum value:", maximum)
            print("Sum of values:", total)
            print("Average value:", round(average, 2))


    # ======================================================
    # OPTION 7 - EXIT
    # ======================================================
    elif choice == "7":

        print("\nThank you for using Functional Treat!")
        print("Goodbye!")

        break


    # ======================================================
    # INVALID CHOICE
    # ======================================================
    else:

        print("\nInvalid choice!")
        print("Please select a number from 1 to 7.")
