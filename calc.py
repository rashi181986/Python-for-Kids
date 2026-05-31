def add(x, y):
    z=x+y
    print(z)

def sub(x, y):
    z=x-y
    print(z)

def div(x, y):
    z=x/y
    print(z)

def mul(x, y):
    z=x*y
    print(z)

a=int(input("Enter the first number "))
b=int(input("Enter the first number "))
c=input("Options add, sub, mul, div ")
if(c=="add"):
    add(a,b)
elif(c=="sub"):
    sub(a,b)
elif(c=="mul"):
    mul(a,b)
elif(c=="div"):
    div(a,b)
else:
    print("Invalid Option")

