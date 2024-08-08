""" A-2: Write a program to read a number and check whether it is divisible by
a given number."""

n = int(input("Enter a number: "))
d = int(input("Enter the divisor: "))

if n % d == 0:
    print(n, "is divisible by", d)
else:
    print(n, "is not divisible by", d)
