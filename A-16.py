""" A-16: Government of India has decided to give scholarships for students who
are first graduates in family and have scored average > 98 in math,
physics, and chemistry. Design an algorithm and write a Python
program to check if a student is eligible for scholarship. (Boundary
Conditions: All marks should be >0 ) """


m=int(input('Write the marks in Mathmatics subject :-'))
p=int(input('Write the marks in Physics subject :-'))
c=int(input('Write the marks in Chemistry subject :-'))

avg=(m+p+c)/3

if m<0 or p<0 or c<0:
    print('Invalid Score Entered !')

elif avg>=98:
    print('          Congratulation! \nYou Have Qualified For The Scholarship :)' )
    print(' Your average marks was :',avg)
else:
    print('         Regret! \nYou Failed To Get Scholarship :(')
    print(' Your average marks was :',avg)