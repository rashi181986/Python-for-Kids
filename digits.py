# Program to count the number of digits

number = int(input("Enter a number: "))

count = len(str(abs(number)))

print("Total digits =", count)