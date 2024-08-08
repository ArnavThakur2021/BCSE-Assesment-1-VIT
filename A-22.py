# A-22:Program to print all numbers in a range divisible by a given number ‘n’


def find_divisibles(lower, upper, n):
    print(f"Numbers divisible by {n} between {lower} and {upper} are:")
    for i in range(lower, upper + 1):
        if i % n == 0:
            print(i)

lower = int(input("Enter the lower range limit: "))
upper = int(input("Enter the upper range limit: "))
n = int(input("Enter the number to divide by: "))2
find_divisibles(lower, upper, n)