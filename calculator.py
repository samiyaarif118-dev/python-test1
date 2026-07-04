print("Calculator")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

choice = input("Choose a number between (1 - 4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")


if choice == "1": 
     print(num1, "+", num2, "=", add(num1, num2))
elif choice =="2":
        print(num1, "-", num2, "=", subtract(num1, num2))
elif choice =="3":
        print(num1, "*", num2, "=", multiply(num1, num2))
elif choice =="4":
     print(num1, "/", num2, "=", divide(num1, num2))
else:
     print("Please choose a number between 1 to 4")





