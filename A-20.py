""" A-20 :- Write a program to define two complex numbers and then read a
choice (menu with 1. Find Sum 2. Subtraction 3. Multiply) to do the
corresponding operation. """

def complex_operations(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    else:
        return "Invalid choice"

num1 = complex(2, 3)
num2 = complex(4, 5)
print("Choose an operation:")
print("1. Find Sum")
print("2. Subtraction")
print("3. Multiply")
choice = int(input("Enter your choice (1/2/3): "))
result = complex_operations(choice, num1, num2)
print(f"The result of the operation is: {result}")