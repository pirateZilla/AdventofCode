inputFile = open("inputs/modules.txt", "r")

sum_fuel = 0
for i in inputFile:
	mass = int(i)
	fuel = (mass/3) - 2
	total_fuel = fuel
	while (fuel > 0):
		fuel = (fuel/3) - 2
		if (fuel > 0):
			total_fuel = total_fuel + fuel
	sum_fuel = sum_fuel + total_fuel

print(sum_fuel)