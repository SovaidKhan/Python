#time.py
#Sovaid Khan
#Data validation

int_hours = eval(input("Enter the hours: "))
int_minutes = eval(input("Enter the minutes: "))
int_seconds = eval(input("Enter the seconds: "))

valid = "Your time is valid."
invalid = "Your time is invalid."

if (int_hours < 0 or int_hours > 23):
    print(invalid)
elif (int_minutes < 0 or int_minutes > 59):
    print(invalid)
elif (int_seconds < 0 or int_seconds > 59):
    print(invalid)
else: print(valid)