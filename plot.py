import math #all a0rbitary functions
function = input("Enter a function f(x):\n")
for y in range(10,-11,-1):
  for x in range(-10,11):
    # eval calculates the function as it was inputted, 
    # also necessary for this to begin the if condition since 
    # when it comes to printing on the axes, 
    # the other conditions might suffice but we need an 'o' there instead of a dash
    if y == round(eval(function)):
        print("o", sep="", end= "")    
    elif y == 0 and x != 0:
      # instead of a dash, because this is the axis, 
      # utilize the hyphen instead to make the points equidistant from the axes
      print("-", sep="", end= "")
    elif y == 0 and x == 0:
      print("+", sep="", end= "")
    elif y!= 0 and x == 0:
        print("|", sep="", end= "")
    else:
      print(" ", sep="", end= "")
  print("") #move to the next line in the Y axis
