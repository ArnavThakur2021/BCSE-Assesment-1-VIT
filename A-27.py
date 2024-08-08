# A-27: Program to check whether the input string is a palindrome or not 

def is_palindrome(s):
    # Convert the string to lowercase to make the check case-insensitive
    s = s.lower()
    reversed_s = s[::-1]
    return s == reversed_s

input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print(f"'{input_str}' is a palindrome.")
else:
    print(f"'{input_str}' is not a palindrome.")