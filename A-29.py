# A-29:-Write a program to display all odd multiples of an odd number ‘n’ (in arange)

def odd_multiples(n, start, end):
    if n % 2 == 0:
        print("Please enter an odd number for 'n'.")
        return
    
    for i in range(start, end + 1):
        if i % n == 0 and i % 2 != 0:
            print(i, end=" ")

n = int(input("Enter an odd number 'n': "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
odd_multiples(n, start, end)