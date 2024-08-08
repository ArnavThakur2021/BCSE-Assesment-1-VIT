# A-24: Write a python program for factorial of a number n 

def factorial(n):
    if n == 0:
        return 1
    else:
        fact = 1
        for i in range(1, n+1):
            fact *= i
        return fact
        
num = int(input("Enter a number: "))
if num < 0:
    print("Error: Factorial is not defined for negative numbers.")
else:
    fact = factorial(num)
    print("Factorial of", num, "is", fact)


