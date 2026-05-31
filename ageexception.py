# Program to check age using exceptions

try:
    age = int(input("Enter your age: "))

    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")

    print("Valid age entered.")

except ValueError as e:
    print("Invalid input:", e)