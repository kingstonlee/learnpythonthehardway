def inc_num(number, increment):
	i = 0
	numbers = []

	while i < number:
		print "At the top i is %d" % i
		numbers.append(i)
	
		i = i + increment
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i
	
	print "The numbers: "

	for num in numbers:
		print num
		
inc_num(7, 5)