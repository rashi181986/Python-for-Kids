print("Hello, welcome to this very basic calculator")
user_input = int(input("Enter how many calculations do you want to do: "))
print("Start by entering the two numbers for conducting calculation")

for i in range(user_input):
  add = 0
  sub = 0
  mul = 0
  div = 0
  quo = 0
  rem = 0
  exp = 0

  num1 = int(input("Enter first number: "))
  num2 = int(input("Enter second number: "))


  add = num1 + num2
  sub = num1 - num2
  mul = num1 * num2
  div = num1 / num2
  quo = num1 // num2
  rem = num1 % num2
  exp = num1 ** num2

  print("The addition of the two numbers is ",add)
  print("The subtraction of the two numbers is ",sub)
  print("The multiplication of the two numbers is ",mul)
  print("The division of the two numbers is ",div)
  print("The quotient of the two numbers is ",quo)
  print("The remainder of the two numbers is ",rem)
  print("The exponent of the two numbers is ",exp)
