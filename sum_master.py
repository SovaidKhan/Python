#Mergesort just for fun can use a simple sort
def MergeSort(SumArray):
    if len(SumArray)> 1:
        mid = len(SumArray)//2
        L = SumArray[:mid]
        R = SumArray[mid:]
        MergeSort(L)
        MergeSort(R)
        i = 0
        j = 0
        k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                SumArray[k] = L[i]
                i += 1
            else:
                SumArray[k] = R[j]
                j += 1
            k += 1   
        while i < len(L):
            SumArray[k] = L[i]
            i +=1
            k +=1
        while j < len(R):
            SumArray[k] = R[j]
            j +=1
            k +=1        
    return SumArray        
def sum_master(Array):
    SumArray = []
    for i in range(0,len(Array)-1):
        for y in range(i,len(Array)-1):
            try:
                j = Array.index(Array[i]+Array[y+1])
                if j >= 0:
                    try:
                        SumArray.index(Array[j])
                    except ValueError:
                        SumArray.append(Array[j])
            except ValueError:
                pass
    return MergeSort(SumArray)
