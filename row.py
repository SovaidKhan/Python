#row.py
#Sovaid Khan
#the user to enter a number, n, where -6<n<93. The
#program will print a sequence of 7 numbers, starting from that value

start_num = eval(input("Enter the start number: "))

for n in range (0,7):
    print('{0:>2}'.format(str(start_num+n)),"", end='') #right justified fixed width 2
    
    
 