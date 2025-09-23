import random

def play():
	user = input("make a choice! \n 's' for scissor, 'p' for paper, 'r' for rock;  \n").lower()
	computer = random.choice(['s', 'p', 'r'])
	
	if user == computer:
		return "it's a tie."
	
	if is_win(user, computer):
		return "you won!"

	return "you lost.."
		
def is_win(player, opponent):
	if (player =='r' and opponent == 's') or (player =='p' and opponent == 'r') or (player =='s' and opponent == 'p'):
		return True
	

print(play())