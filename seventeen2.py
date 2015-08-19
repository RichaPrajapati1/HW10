##############################################################################
################################ IMPORTS: ####################################
##############################################################################
import random

##############################################################################
############################ GLOBAL VARIABLES: ###############################
##############################################################################

MarblesInJar = 17

##############################################################################
############################## FUNCTIONS: ####################################
##############################################################################

def Player2_input():
	global MarblesInJar
	RandomNum = random.randint(1,3)
	if RandomNum > MarblesInJar:
		return Player2_input()
	return RandomNum

def Player1_input(num):
	global MarblesInJar
	if num > MarblesInJar:
		return MarblesInJar
	else:
		return num
	
def play_game():
	global MarblesInJar
	GameNum = 1
	PlaySequence = []
	open("seventeen2_output.txt", 'w').close()
	fout = open("seventeen2_output.txt","a")
	with open("i206_placein_input_0.txt","r") as fin:
		for line in fin:
			MarblesInJar = 17
			PlaySequence = []
			fout.write("Game #" + str(GameNum) + " Play Sequence: ")
			current_list = line.strip().split(',')
			print current_list
			for idx,num in enumerate(current_list):
				Player1 = Player1_input(int(num))
				fout.write(str(Player1)+'-')
				MarblesInJar = MarblesInJar - Player1
				if MarblesInJar == 0:
					fout.write(". Winner: P2\r\n")
					break
				Player2 = Player2_input()
				fout.write(str(Player2)+'-')
				MarblesInJar = MarblesInJar - Player2
				if MarblesInJar == 0:
					fout.write(". Winner: P1\r\n")
					break
			GameNum += 1
	fout.close()


##############################################################################
################################ MAIN: #######################################
##############################################################################
def main():
	# print ("Let's play the game of Seventeen!")
	# print ("Number of marbles left in jar: 17")
	play_game()



if __name__ == '__main__':
    main()