#palindromeprime.py
#SovaidKhan
#that finding all palindromic primes between two
#integers supplied as input (start and end points are excluded)

a =eval(input("Enter the start point N:\n"))           #loop needsto take in int so eval first
b =eval(input("Enter the end point M:\n"))
print("The palindromic primes are:")
p=0         #set p default for 2 for intial no runnng of the loop ie for i = 2 where for j doesnt run
for i in range(a+1,b):      #range not included
    if str(i)[::-1] == str(i):      #reverse  
        for j in range(2, i  ,1):    #prime number not checkint(i**0.5)+1
            if i%j == 0 or i%2 ==0:
                p = 1
                break
            else:
                p = 0
        if p ==0:
            print(i)
    
    
    
    
    
    
    
    
    
    #for j in range(0,9):
    
    #    if i%j != 0:
     
     #       break
    