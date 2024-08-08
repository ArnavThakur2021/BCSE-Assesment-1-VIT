# A-32:Program to list all Fibonacci numbers in a given range.

def fibonacci_in_range(start, end):
    a, b = 0, 1
    fib_list = []

    while a <= end:
        if a >= start:
            fib_list.append(a)
        a, b = b, a + b
    return fib_list

start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
fib_numbers = fibonacci_in_range(start, end)
print(f"Fibonacci numbers in the range {start} to {end}: {fib_numbers}")