def coprime(Array):
    count = 0
    for i in range(0,len(Array)-1):
            for y in range(i,len(Array)-1):
                flag = True
                for k in range(2,9):
                    if Array[i]%k == Array[y+1]%k == 0:
                        flag = False
                        break
                if flag == True:
                    count +=1
    return count   