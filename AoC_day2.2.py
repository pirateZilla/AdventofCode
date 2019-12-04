for x in range(100):
	for y in range(100):
		input = open("inputs/outcode.txt", "r")
		codes = map(int, input.read().split(","))

		codes[1] = x
		codes[2] = y

		for i in range(0, len(codes), 4):
			first = codes[i]
			second = codes[i+1]
			third = codes[i+2]
			fourth = codes[i+3]
			if (first == 1):
				codes[fourth] = codes[second] + codes[third]
			elif (first == 2):
				codes[fourth] = codes[second] * codes[third]
			elif (first == 99):
				break

		if (codes[0] == 19690720):
			print(x)
			print(y)
			print((100*x) + y)

#codes[0] = 19690720