def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


print("============================")
print("1. TO PERFORM ADDITION")
print("2. TO PERFORM SUBTRACTION")
print("3. TO PERFORM MULTIPLICATION")
print("4. TO PERFORM DIVISION")
print("5. EXIT")
print("============================")

while True:
    choice = int(input("Enter your choice: "))

    if choice == 1:
        a = int(input("Enter the 1st value: "))
        b = int(input("Enter the 2nd value: "))
        print("Result:", add(a, b))

    elif choice == 2:
        a = int(input("Enter the 1st value: "))
        b = int(input("Enter the 2nd value: "))
        print("Result:", sub(a, b))

    elif choice == 3:
        a = int(input("Enter the 1st value: "))
        b = int(input("Enter the 2nd value: "))
        print("Result:", mul(a, b))

    elif choice == 4:
        a = int(input("Enter the 1st value: "))
        b = int(input("Enter the 2nd value: "))
