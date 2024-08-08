"""A-28:- Write a menu-driven program that gets the user chooses to perform
add/sub/mul/div with the obtained two inputs """

def int_operations(choice, num1, num2):
    if choice == 1:
        return num1 + num2
    elif choice == 2:
        return num1 - num2
    elif choice == 3:
        return num1 * num2
    elif choice== 4:
        return num1/num2
    else:
        return "Invalid choice"

num1 = int(input('Enter first number:-'))
num2 = int(input('Enter second number:-'))
print("Choose an operation:")
print("1. Find Sum")
print("2. Subtraction")
print("3. Multiply")
print("4. Division")
choice = int(input("Enter your choice (1/2/3/4): "))
result = int_operations(choice, num1, num2)
print(f"The result of the operation is: {result}")