import random
"""this program promtes the compiter to guess a number we are thinking about, and we let it know which it is"""

def computer_guess(x):
	low = 1
	high = x
	feedback = ' '
	print("guess a number between 1 and 10") #its up to you to determine what the max number is, for the computer to guess from
	while feedback != 'c':
		if low != high:
			guess = random.randint(low, high)
		else:
			guess = low #could be high/low, doesn't matter'
		feedback = input(f"is {guess} too high(H),too low(L) or correct (C)?? ").lower()
		if feedback == 'h':
			high = guess - 1
		elif feedback == 'l':
			low = guess + 1
		elif feedback != 'c':
			print("wrong option! go again.")
	
	print(f"yay! th computer guessed your number, {guess}, correctly!!")
	

computer_guess(10)