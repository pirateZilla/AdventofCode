input = open("inputs/outcode.txt", "r")
codes = map(int, input.read().split(","))

codes[1] = 12
codes[2] = 2

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

print(codes[0])