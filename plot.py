import math #all a0rbitary functions
function = input("Enter a function f(x):\n")
for y in range(10,-11,-1):
  for x in range(-10,11):
    if y == round(eval(function)):
        print("o", sep="", end= "")    
    elif y == 0 and x != 0:
      print("-", sep="", end= "")
    elif y == 0 and x == 0:
      print("+", sep="", end= "")
    elif y!= 0 and x == 0:
        print("|", sep="", end= "")
    else:
      print(" ", sep="", end= "")
  print("\n",end="") #no newline space














