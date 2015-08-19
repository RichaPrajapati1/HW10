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
def user_input():
	global MarblesInJar
	
	while True: 
		print ("")
		UserInput = raw_input("Your turn: How many marbles will you remove (1-3)? ")
		try:
			InputNum = int(UserInput)
		except:
			print ("Sorry, that is not a valid option. Try again!")
			print ("Number of marbles left in jar: {0}" .format(MarblesInJar))
			continue
		else:
			if InputNum <= 0 or InputNum > 3:
				print ("Sorry, that is not a valid option. Try again!")
				print ("Number of marbles left in jar: {0}" .format(MarblesInJar)) 
				continue
			elif InputNum > MarblesInJar:
				print ("Sorry, that is not a valid option. Try again!")
				print ("Number of marbles left in jar: {0}" .format(MarblesInJar)) 
				continue
			else:
				break
	return InputNum

def count_remaining(User,MarblesPicked,NextPlayer):
	global MarblesInJar
	MarblesInJar = MarblesInJar - MarblesPicked
	print ("{0} removed {1} marbles" .format(User,MarblesPicked))
	if MarblesInJar == 0:
		print("")
		print ("There are no marbles left. {0} win!" .format(NextPlayer))
		return
	else:
		print ("Number of marbles left in jar: {0}" .format(MarblesInJar))
		return

def pick_generator():
	global MarblesInJar
	RandomNum = random.randint(1,3)
	if RandomNum > MarblesInJar:
		return pick_generator()
	return RandomNum

def play_game():
	global MarblesInJar
	while True:
		UserInput = user_input()
		count_remaining('You',UserInput,'Computer')
		if MarblesInJar == 0:
			break
		print ("")
		print ("Computer's turn...")
		ComputerInput = pick_generator()
		count_remaining('Computer',ComputerInput,'You')
		if MarblesInJar == 0:
			break
		else:
			continue


##############################################################################
################################ MAIN: #######################################
##############################################################################
def main():
	print ("Let's play the game of Seventeen!")
	print ("Number of marbles left in jar: 17")
	play_game()



if __name__ == '__main__':
    main()