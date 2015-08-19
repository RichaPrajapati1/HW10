def len_list(n):
	counter = 0
	for thing in n:
		counter += 1
	return counter

def main():
	list1 = [1,2,3]
	string = 'richa'
	d = {1:'one', 2:'two'}
	t = (1,2,3,4)
	print  len_list(list1)
	print  len_list(string)
	print  len_list(d)
	print  len_list(t)

if __name__ == '__main__':
    main()
