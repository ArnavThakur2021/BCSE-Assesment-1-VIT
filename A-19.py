""" A-19 : Write a program to read an integer and convert it to binary, octal and
hex numbers. """

def convert_num(num):
    b = bin(num)
    o = oct(num)
    h = hex(num)
    return b, o, h
num = int(input("Enter an integer : "))

# Convert the number
b, o, h = convert_num(num)

# Display the results
print(f"The decimal value of {num} is:")
print(f"{b} in Binary.")
print(f"{o} in Octal.")
print(f"{h} in Hexadecimal.")