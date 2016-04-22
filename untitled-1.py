def t(sentence):
      
      while sentence.find('ay') != -1 : #only as many as needed
            front = ''
            i_1 = sentence.find('ay') # gto x part of xay 'ay' not 'ay ' becasue of ennding with ay
            i_2 = i_1 -1
            while sentence[i_2] != 'a' and i_2 >=0:
                  i_2 -= 1     
            front += sentence[i_2:i_1]
            sentence= sentence[:i_2-len(front)-1] + front +sentence[:i_2] + '' + sentence[i_1+3:]
            
      return front, sentence
