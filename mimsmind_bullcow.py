def get_bullcow(guess, rand_num):
    # This function uses a loop to count the number of bulls first
    # It then counts the number of cows. But the bulls are double-
    # counted in the cows which are removed from the final cow count
    # It then prints the number of cows and bulls
    Bull = 0
	Cow = 0
	for i in range(len(guess)):		#This loop will count the number of bulls
		for j in range(len(rand_num)):
			if guess[i] == rand_num[j] and i == j:
				Bull += 1
				break
	Temp_Num_Str = rand_num 				#Making a temporary variable to store the random generated number for the next guess
	for letter in guess:				#This loop will count the number of cows (including bulls)
		if letter in Temp_Num_Str:
			index = Temp_Num_Str.find(letter)
			Cow += 1
			Temp_Num_Str = Temp_Num_Str[:index] + Temp_Num_Str[index+1:]
						
	Cow = Cow - Bull					#Removing the double counts in cows
	guess = raw_input("{0} bull(s), {1} cow(s). Try again: " .format(Bull,Cow))
	return