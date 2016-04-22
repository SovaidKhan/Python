#pi.py
#Sovaid Khan
#program that calculates the value of PI and then computes and displays the
#area of a circle with radius entered by the user

import math

a = 0

pi = 2
next_term = 0

while next_term != 1:
    a = 2 + math.sqrt(a)
    denom = math.sqrt(a)
    next_term = 2/denom

    pi = pi * next_term
    
print("Approximation of pi:",round(pi,3))
r = eval(input("Enter the radius: \n"))
Area= pi*r**2       #^ is bitwise OR Python ** is power
print("Area:",round(Area,3))


