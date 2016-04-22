import string
def pangram_check(sentence):
    Check = [False]*26
    Alphabet =list(string.ascii_letters)
    for i in range(0,len(sentence)):
        try:
            j = Alphabet.index(sentence[i])
        except ValueError:
            j = -1    
        if j >= 26:
            j-=26
        if j != -1:
            Check[j] = True   
    try:
        if Check.index(False) > -1:
            return False
    except ValueError:
        return True
#50 mins