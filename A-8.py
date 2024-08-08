#A-8: Write a program to swap two variables without using a third variable.

x=input('Enter first number')
y=input('Enter second number')
print("Before Swapping Numbers Are:",(x,y))
x, y = y, x
print("After swapping Numbers Are:",(x,y))
