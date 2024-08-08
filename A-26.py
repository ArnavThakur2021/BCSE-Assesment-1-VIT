# A-26: Program to check whether the input number is a palindrome or not 

def is_palindrome(num):
    str_num = str(num)
    reversed_str_num = str_num[::-1]
    return str_num == reversed_str_num

num = int(input("Enter a number: "))
if is_palindrome(num):
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")