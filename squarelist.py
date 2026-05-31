# Create a list of square values and separate odd and even values

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

squares = []

for i in range(start, end + 1):
    squares.append(i ** 2)

even_squares = []
odd_squares = []

for num in squares:
    if num % 2 == 0:
        even_squares.append(num)
    else:
        odd_squares.append(num)

print("Square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)