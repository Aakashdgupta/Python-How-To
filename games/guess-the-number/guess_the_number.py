''' Guess The Number Implementation Both Computer and User Version 
''' 

def guess(rand,Life):
	
	if Life <1:
		return False
	ans = input(f"Enter a number between 1 and 50 you you have {Life} Life.  ")
	
	ans= int(ans)
	if ans > rand:
		print("too high")

		return guess(rand,Life-1)
	elif ans < rand:
		print("too low")
		
		
		return guess(rand,Life-1)
	else:
		return True
		
while True:
	
	print(" 1. I will guess number")
	print(" 2. let the Computer Guess")
	print("3. Quit")
	choice = input("Enter your choice? ")
	if choice == "3":
		break

	if choice == "1":
		import random
		randN = random.randint(1,50)
		won = guess(randN,10)
		if won:
			print("You Won !")
	else :
		print("Choose a number between 1 and 50")
		print('guessing.........................')

		import time
		time.sleep(5)

		LeftGuessLimit =1
		RightGuessLimit=51
		Life=10
		won=False
		while Life>0:
			import random
			randC = random.randint(LeftGuessLimit,RightGuessLimit)
	
			PlayerAns = input(f"\n      guess = {randC} \n     enter L for low \n     H for High  \n     E for equal  \n     life Left ={Life}/10 ")
			if PlayerAns =="H" or "h":
				Life -= 1
				RightGuessLimit = randC-1
			elif PlayerAns=="L" or "l":
				Life -=1
				LeftGuessLimit = randC+1
			else:
				won =True
				break
		if won :
			print("Computer Won!")
		else:
			print("You Won")