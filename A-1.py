#Write a program to read a number and check whether it is even or odd

print('Give A Number :')
num=int(input())
# Check if the number is even or odd
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")
