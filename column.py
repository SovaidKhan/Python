#column.py
#Sovaid Khan
#that asks the user to enter a number, n, where -6<n<2.
#Starting from n, the program will print out every 7th number in the range n to n+41.

start_num = eval(input("Enter a number: "))
i =0
if start_num >-6 and start_num <2:
    for n in range (start_num,start_num+41,7):  #range skip 7
        print('{0:>2}'.format(str(start_num+7*i)),"", end='\n') #right justified fixed width 2
        #add 7 depedning on teration  ..because start um and n both start at -5 so firstbecomes -10
        i+=1
        

    
 