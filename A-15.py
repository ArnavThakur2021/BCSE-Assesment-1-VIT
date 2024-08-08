"""A-15 :- Little Bob loves chocolate, and he goes to a store with Rs. Nin his
pocket. The price of each chocolate is Rs. C. The store offers a discount:
for every M wrappers he gives to the store, he gets one chocolate for
free. This offer is available only once. How many chocolates does Bob
get to eat? Write a program that solves this problem."""

def chocolates(N, C, M):
    chocolates_bought = N // C
    wrappers = chocolates_bought
    additional_chocolates = wrappers // M
    total_chocolates = chocolates_bought + additional_chocolates

    return total_chocolates
N = int(input("Enter the amount of money Bob has (Rs): "))
C = int(input("Enter the price of each chocolate (Rs): "))
M = int(input("Enter the number of wrappers needed for one free chocolate: "))

result = chocolates(N, C, M)
print(f"Bob can eat a total of {result} chocolates.")