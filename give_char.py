import random
import pygame



def givechar(cap_char) :
	
	n=len(cap_char)
	shit_char= ['!','@','#','$','%','^','&','*','(',')','<','>']

	intres=['a','d','e','o','w']

	com_1=['s','a','v','e']

	com_2=['l','o','w']

	com_3=['x','t','w','o']

	com_4=['s','h','i','e','l','d']

	com_5=['b','c','f','g','i','j','k','m','n','p','q','r','u','y','z']
 
	space=[' ']*20

	#save has not yet been captured.
	if 's' not in cap_char or 'a' not in cap_char or 'v' not in cap_char or 'e' not in cap_char:

		#print("i am in if")
		search=[]
		search.extend(com_1*3)
		search.extend(com_2)
		search.extend(shit_char)
		search.extend(intres)
		search.extend(space)
		search.extend(com_4)
		search.extend(com_5)
		ch=random.choice(search)
		
		return ch

	#slow has not yet benn captured
	elif 'l' not in cap_char or 'o' not in cap_char or 'w' not in cap_char:

		#print("i am in if")
		search=[]
		search.extend(com_1)
		search.extend(com_2*2)
		search.extend(shit_char)
		search.extend(intres)
		search.extend(com_4)
		search.extend(space)
		search.extend(com_5)
		ch=random.choice(search)
		
		return ch
	
	else:

		search=[]
		search.extend(com_1)
		search.extend(shit_char)
		search.extend(com_2)
		search.extend(intres)
		search.extend(com_4)
		search.extend(com_5)
		search.extend(com_3)
		search.extend(space)
		ch=random.choice(search)
		
		return ch
'''if __name__=="__main__" :

	cap_char=[2,3]
	ch='_'
	while(ch!= None) :
		ch=givechar(cap_char)
		cap_char.append(ch)


	print(givechar(['s','a','v']))'''
		
