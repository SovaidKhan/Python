#firstday.py
#Sovaid Khan
#asks the user to enter a year range and that prints out
#the name of the day on which the 1st of January falls for each year in that range.

First_year = eval(input("Enter the first year:\n"))
Second_year = eval(input("Enter the second year:\n"))


#Gauss' 

# %

Current_year = First_year 

while Current_year < Second_year + 1:

    day_num = ((1 + 5*((Current_year - 1)%4)) + 4*((Current_year - 1)%100) + 6*((Current_year - 1)%400))%7
    
    if day_num == 0:
        day = "Sunday"
    elif day_num == 1:
        day = "Monday"  
    elif day_num == 2:
        day = "Tuesday"
    elif day_num == 3:
        day = "Wednesday"
    elif day_num == 4:
        day = "Thursday"
    elif day_num == 5:
        day = "Friday"
    elif day_num == 6:
        day = "Saturday"
    
    print("The 1st of January ",Current_year," falls on a ",day,".", sep='')
    Current_year += 1
    