# A-33: Program to check whether a given number is a Fibonacci number or not

import math

def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x

def is_fibonacci(n):
    # A number is a Fibonacci number if and only if one or both of (5*n^2 + 4) or (5*n^2 - 4) is a perfect square
    return is_perfect_square(5 * n * n + 4) or is_perfect_square(5 * n * n - 4)

num = int(input("Enter a number: "))
if is_fibonacci(num):
    print(f"{num} is a Fibonacci number.")
else:
    print(f"{num} is not a Fibonacci number.")