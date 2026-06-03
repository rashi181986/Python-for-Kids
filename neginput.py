def take_input():
    num = int(input("Enter a number: "))

    # Base case
    if num < 0:
        print("Negative number entered. Program stopped.")
        return

    # Recursive call
    take_input()

# Start the recursion
take_input()