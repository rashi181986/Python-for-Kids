# Program to find the product of all numbers in a tuple

numbers = (2, 3, 4, 5)

product = 1

for num in numbers:
    product = product * num

print("The tuple is:", numbers)
print("The product of all numbers is:", product)