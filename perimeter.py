#program to calculate perimiter cost
#perimeter.py
#Sovaid Khan
#24 February 2016

w1 = eval(input("Enter width 1: "))
h1 = eval(input("Enter height 1: "))
w2 = eval(input("Enter width 2: "))
h2 = eval(input("Enter height 2: "))
ppm = eval(input("Enter price per metre: "))

T_fence = 2*h1 + 2 * w1 + 2 * w2
print("The total fence required =", T_fence, "metres")

T_price = T_fence * ppm

print("The total price = R", T_price)