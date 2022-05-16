'''Hangman Game implementation'''

import random

words =["TIGER","LION","PYTHON","HORSE","SHEEP"]

def hangman():
	Cword= random.choice(words)
	usedL=[]
	
	hint = random.choice(Cword)
	
	usedL.append(hint)
	#print(hint)
	
	
	print("Current Word :",end=' ')
	for letter in Cword:
		if letter==hint:
			print(letter,end='')
		print("_",end='')

	print()
	
	Cword=[n for n in Cword]
	life=len(Cword)+4
	#print(Cword)
	
	won=0
	
	while life >0:
		#Check for Victory
		if won == len(Cword):
			break
		
		

		print()
		print(f"Life = {life} ")
		userL=input("Guess a Letter : ")
	
		if userL not in usedL:
			usedL.append(userL)
			
			#printing used letters
			print()
			print("You already used : ")
			for L in usedL:		
				print(L,end=" , ")
			#print(usedL)
		print()
		print("Current Word : ",		end='')
		
		#reseting won before itteration
		won =0
	
		for L in Cword:
			
			if L in usedL:
				print(L,end='')
				#increamenting won means number of finished letter = won
				won += 1
				
				
			else:
				print("_",end='')
		life -= 1
			
	
	
	
	
	

hangman()
	