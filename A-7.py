# A-7: Write a program to read a number and calculate its square root.

import math
num = float(input("Enter a number: "))
if num < 0:
    print("Error: Square root of negative numbers is not a real number.")
else:
    sqrt = math.sqrt(num)
    print("Square root of", num, "is", sqrt)
