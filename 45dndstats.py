# authors: Mo, Aidan

import random

def R3D6():
	return random.randint(1, 6) + random.randint(1, 6) + random.randint(1, 6)

def R3D6r1():
	roll1 = random.randint(1, 6)
	roll2 = random.randint(1, 6)
	roll3 = random.randint(1, 6)
	# Keep rerolling 1s until there are no 1s if there are 1s
	while roll1 == 1:
		roll1 = random.randint(1, 6)
	while roll2 == 1:
		roll2 = random.randint(1, 6)
	while roll3 == 1:
		roll3 = random.randint(1, 6)
	return roll1 + roll2 + roll3

def R3D6x2():
	roll = 0
	for i in range(3):
		roll1 = random.randint(1, 6)
		roll2 = random.randint(1, 6)
		if roll1 > roll2:
			roll += roll1
		else:
			roll += roll2
	return roll

def R4D6d1():
	roll = 0
	# rolls can never be higher than 7
	lowest_roll = 7 

	for i in range(4):
		current_roll = random.randint(1, 6)
		roll += current_roll

		if current_roll < lowest_roll:
			lowest_roll = current_roll
	# Remove lowest roll
	roll -= lowest_roll
	return roll

# Test averages
n = 1000000
total_R3D6 = 0
total_R3D6r1 = 0
total_R3D6x2 = 0
total_R4D6d1 = 0
for i in range(n):
	total_R3D6 += R3D6()
	total_R3D6r1 += R3D6r1()
	total_R3D6x2 += R3D6x2()
	total_R4D6d1 += R4D6d1()

print("averages:")
print("3D6:", total_R3D6/n)
print("3D6r1:", total_R3D6r1/n)
print("3D6x2:", total_R3D6x2/n)
print("4D6d1:", total_R4D6d1/n)


	