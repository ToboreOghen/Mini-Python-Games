import random
from words import words
import string


def get_valid_word(words):
	word = random.choice(words)
	
	while '-' in word or ' ' in word:
		word = random.choice(words)
		
	return word.upper()
	
	
def hangman():
	word = get_valid_word(words)
	word_letters = set(word)
	alphabets = set(string.ascii_uppercase)
	used_letters = set()
	
	lives = 6
	
	#get user input and continue iteration
	while len(word_letters) > 0 and lives > 0:
		print(f" you have {lives} left and \n you have used these: ", ' '.join(used_letters))
		
		#what current word is (i.e W_RD)
		word_list = [letter if letter in used_letters else '_' for letter in word]
		print("current word: ", ' '.join(word_list))
		
		
		user_letter = input("Guess a letter: ").upper()
		if user_letter in alphabets - used_letters:
			used_letters.add(user_letter)
			if user_letter in word_letters:
				word_letters.remove(user_letter)
			else:
				lives -= 1
				print("letter is not in word.")
		
		elif user_letter in used_letters:
			print("you have already used this letter, try again.")
		else:
			print("invalid character, try again")
	if lives == 0:
		print(f"you died! The word was {word}")
	else:
		print(f"congratulations!! you guessed the word; {word}.")

		
hangman()		