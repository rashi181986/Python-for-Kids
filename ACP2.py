#String
fname = input("Enter your first name")
lname = input("Enter your last name")
age = input("Enter your age")

fullname = fname + " " + lname + " " + "and I am" + " " + age + " " + "years old"

print("My name is", fullname)

print(fullname[10])

print("Cute " * 10)

print("Hey " + "there")

#Operators

num1 = int(input("Enter a number"))
num2 = int(input("Enter a second number"))
num3 = int(input("Enter a third number"))

answer_add = num1 + num2 + num3

print("The answer is ", answer_add)


a = int(input("Enter a number"))
b = int(input("Enter a second number"))

add = a + b
sub = a - b
mul = a * b
div = a / b
quo = a // b
rem = a % b
exp = a ** b

print("The addition is", add)
print("The subtraction is", sub)
print("The multiplication is", mul)
print("The division is", div)
print("The quotient is", quo)
print("The remainder is", rem)
print("The exponent is", exp)