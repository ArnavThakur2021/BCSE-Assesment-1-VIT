#A-31: Program to list all prime numbers within a given range.

n=int(input('Enter The Range For Prime Number:-'))
for i in range(n):
    if i%2 !=0:
        print(i)