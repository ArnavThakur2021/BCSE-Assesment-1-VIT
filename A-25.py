# A-25:	Program to find the sum of digits of a given number. 

def sum_of_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total += digit
        n = n // 10
    return total

n = int(input("Enter a number: "))
result = sum_of_digits(n)
print(f"The sum of the digits of {n} is {result}")