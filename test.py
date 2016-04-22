def to_english(sentence):
	while sentence.find('ay') != -1 : #only as many as needed
        	front = ''
            	i_1 = sentence.find('ay') # gto x part of xay 'ay' not 'ay ' becasue of ennding with ay
		i_2 = i_1-1  #cant be same else a in ay matches
            	while sentence[i_2] != 'a' and i_2 >=0:
			i_2 -= 1     
		i_2 += 1
            	front += sentence[i_2:i_1]
            	sentence= sentence[:i_2-1] + '' + sentence[i_2+len(front)+2:]    
		i_2 -= 2 # to readjust it back for length change
		while sentence[i_2] != ' ' and i_2 > 0:
			i_2 -= 1
		sentence = sentence[:i_2] +' ' + front + sentence[i_2+1:]# +1 to remove space as i_2 is the space postion

	return  sentence
