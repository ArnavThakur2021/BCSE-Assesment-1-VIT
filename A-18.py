""" A-18 :-  Write a program to compute and display the temperature inside the
    earth in Celsius and Fahrenheit.
    The relevant formulas are
    Celsius = 10 x (depth) + 20
    Fahrenheit = 1.8 x (Celsius) + 32   """


d=int(input('Enter The Depth (in metres) :-'))
Celsius = 10*d + 20
Fahrenheit = 1.8*(Celsius) + 32 
print('Temperature inside Earth at this depth is',Celsius,'`Celcius Or',Fahrenheit,'`Fahrenheit')