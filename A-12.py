""" A-12: Write an algorithm to find the average marks of a student. Also check
whether the student has passed or failed. For a student to be declared
pass, average marks should not be less than 65"""

a=int(input('Write the marks in 1st subject'))
b=int(input('Write the marks in 2nd subject'))
c=int(input('Write the marks in 3rd subject'))
d=int(input('Write the marks in 4tb subject'))

avg=(a+b+c+d)/4

if avg>=65:
    print(' Congratulation! You Passed the exams :)' )
    print(' Your average marks was :',avg)
else:
    print(' Regret! You Failed the exams :(')
    print(' Your average marks was :',avg)
    
