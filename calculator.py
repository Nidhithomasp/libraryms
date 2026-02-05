# Simple Calculator Program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b


print("Simple Calculator")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication") 

choice = int(input("Enter your choice (1 or 2): "))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if choice == 1:
    print("Result:", add(num1, num2))
elif choice == 2:
    print("Result:", subtract(num1, num2))
elif choice == 3:             
    print("Result:", divide(num1, num2))

else:
    print("Invalid choice")
