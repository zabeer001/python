# A list in Python is like an array in PHP, but in PHP, the data types of elements are often the same,
# while in Python, the data types can be different.

def sum(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def dev(a, b):
    return a / b

def mod(a, b):
    return a % b

def power(a, b):
    return a ** b

print("""
        Type 
        1 for Sum
        2 for Subtraction
        3 for Multiplication
        4 for Division
        5 for Modulus
        6 for Power
      """)

operation = int(input('Choose an operation: '))

print('Input numbers')

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

""" if operation == 1:
    print("Result:", sum(x, y))
elif operation == 2:
    print("Result:", sub(x, y))
elif operation == 3:
    print("Result:", mul(x, y))
elif operation == 4:
    print("Result:", dev(x, y))
elif operation == 5:
    print("Result:", mod(x, y))
elif operation == 6:
    print("Result:", power(x, y))
else:
    print("Invalid operation selected") """

match operation:
    case 1:
        print("Result:", sum(x, y))
    case 2:
        print("Result:", sub(x, y))
    case 3:
        print("Result:", mul(x, y))
    case 4:
        print("Result:", dev(x, y))
    case 5:
        print("Result:", mod(x, y))
    case 6:
        print("Result:", power(x, y))
    case _:
        print("Invalid operation selected")
