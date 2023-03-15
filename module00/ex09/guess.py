import random

if __name__ == "__main__":
	print("This is an interactive guessing game!\nYou have to enter a number between 1 and 99 to find out the secret number.\nType 'exit' to end the game.\nGood luck!")
	num = random.randint(1, 99)
	print(num)
	attemps = 0
	find = 0
	while(1):
		attemps = attemps + 1
		print("What's your guess between 1 and 99?")
		guess = input(">> ")
		if guess.isdigit():
			if int(guess) == 42:
				print("The answer to the ultimate question of life, the universe and everything is 42.")
				find = 1
			elif int(guess) > num:
				print("Too High!")
			elif int(guess) < num:
				print("Too low!")
			else:
				print("Congratulations, you've got it!")
				find = 1
			if find:
				if attemps == 1:	
					print("Congratulations! You won in your first try!")
				else:
					print("You won in {} attempts!".format(attemps))
				break
		else:
			if guess == "exit":
				print("Goodbye!")
				break
			else:
				print("That's not a number.")
