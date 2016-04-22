#printmonth.py
#Sovaid Khan
#Write a program called 'printmonth.py' that asks the user for a month name and start day and
#then prints the calendar for that month in a 6 row by 7 column grid. (Ignoring issues of leap years,
#assume February has 28 days).


month = input("Enter the month ('January', ..., 'December'): ")
day =  input("Enter the start day ('Monday', ..., 'Sunday'): ")
print(month)
print("Mo Tu We Th Fr Sa Su")

if month == 'January' or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
 last_day = 31
elif month == 'April' or month == 'June' or month == 'September' or month == 'November':
 last_day = 30
elif month == 'February':
 last_day=28
#error?

if day == "Monday":
 start_num = 1   
elif day == "Tuesday":
 start_num = 0      
elif day == "Wednesday": 
 start_num = -1
elif day == "Thursday":
 start_num = -2   
elif day == "Friday":
 start_num = -3
elif day == "Saturday":
 start_num = -4
elif day == "Sunday":
 start_num = -5
  
i=0 #keep i same throughout
if start_num >-6 and start_num <2:
    for n in range (start_num,start_num+41,7):  #range 
        for r in range (0,7):
            if start_num+i>0 and start_num+i <= last_day:
                print('{0:>2}'.format(str(start_num+i)),"", end='') #right justified fixed width 2
                #add 7 depedning on teration  ..because start um and n both start at -5 so firstbecomes -10
                
            else: 
             print('{0:>2}'.format(" "),"", end='')
             
            i+=1 #i keeps going put it ouside if so i executes and moves to next term to be evaluated else gets stuck on 0
            
        print(end='\n')   #indentation on same level!!!!!
        
    
        

    
 