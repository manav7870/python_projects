#Calculator

print("Calculator")
def add(x, y):
    return x + y
def sub(x, y):
    return x - y
def product(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        print("Error!! Denominator can't be zero!!")
    else:
        return x / y
print("1.Addition: +\n2.Subtraction: -\n3.Product: *\n4.Division: /")    
x = int(input("Enter the value of x: "))
y = int(input("Enter the value of y: "))
a = input("Enter your choice (+, -, *, /): ")
if a == "+":
    result = add(x, y)
elif a == "-":
    result = sub(x, y)
elif a == "*":
    result = product(x, y)
elif a == "/":
    result = divide(x, y)
else:
    print("Invalid Operator!!")
print("Result: ",result)    