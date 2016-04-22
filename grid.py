#grid.py
#Sovaid Khan
# accepts a number, n, where -6<n<2. The program will print
#out the numbers n to n+41 as 6 rows of 7 numbers. The first row will contain the values n to n+6, the
#second, the values n+7 to n+7+6, and so on


start_num = eval(input("Enter the start number: "))
i=0 #keep i same throughout
if start_num >-6 and start_num <2:
    for n in range (start_num,start_num+41,7):  #range 
        
        for r in range (0,7):
            print('{0:>2}'.format(str(start_num+i)),"", end='') #right justified fixed width 2
            #add 7 depedning on teration  ..because start um and n both start at -5 so firstbecomes -10
            i+=1 #i keeps going
        print(end='\n')   #indentation on same level!!!!!
        
    
        

    
 