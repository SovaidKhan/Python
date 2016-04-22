#cupcake.py
#Sovaid Khan
#program to determine whether or not you should eat the cupcake

Decision1 = "Decision: Your call."
Decision2 = "Decision: Eat it."
Decision3 = "Decision: Don't eat it."


print("Welcome to the 30 Second Rule Expert")
print("------------------------------------")
print("Answer the following questions by selecting from among the options.")

response= input("Did anyone see you? (yes/no)\n")

if response == 'yes':
        response= input("Was it a boss/lover/parent? (yes/no)\n")
        if response =='yes':
                response= input("Was it expensive? (yes/no)\n")
                if response =='yes':
                        response= input("Can you cut off the part that touched the floor? (yes/no)\n")
                        if response =='yes':
                                print(Decision2)
                        else:
                                print(Decision1)                        
                else:
                        response= input("Is it chocolate? (yes/no)\n")        
                        if response =='yes':
                                print(Decision2)
                        else:
                                print(Decision3)        
        else:
                print(Decision2)
    
else:
        response= input("Was it sticky? (yes/no)\n")
        if response =='yes':
                response= input("Is it a raw steak? (yes/no)\n")
                if response =='yes':
                        response= input("Are you a puma? (yes/no)\n")
                        if response =='yes':
                                print(Decision2)
                        else:
                                print(Decision3)
                else:
                        response= input("Did the cat lick it? (yes/no)\n")
                        if response =='yes':
                                response= input("Is your cat healthy? (yes/no)\n")
                                if response =='yes':
                                        print(Decision2)
                                else:
                                        print(Decision1)
                        else:
                                print(Decision2)
        else:
                response= input("Is it an Emausaurus? (yes/no)\n")
                if response =='yes':
                        response= input("Are you a Megalosaurus? (yes/no)\n")
                        if response =='yes':
                                print(Decision2)
                        else:
                                print(Decision3)
                else:
                        response= input("Did the cat lick it? (yes/no)\n")
                        if response =='yes':
                                response= input("Is your cat healthy? (yes/no)\n")
                                if response =='yes':
                                        print(Decision2)
                                else:
                                        print(Decision1)
                        else:
                                print(Decision2)                
                    
                
                
            
 
       
       
       
       
       








