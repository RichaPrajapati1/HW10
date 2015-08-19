def numbered_lines():
	counter = 1
	fout = open("print.txt","w")
	with open("small.txt","rb") as fin:
		line = fin.read().strip().split("\n")
		for text in line:
			fout.write(str(counter) +" " +text +'\n') 
			counter += 1
	fout.close()

##############################################################################
def main():  # CALL YOUR FUNCTION BELOW
	numbered_lines()


if __name__ == '__main__':
    main()