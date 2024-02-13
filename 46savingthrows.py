# authors: Mo, Aidan

import random

def normal_roll():
	return random.randint(1, 20)

def advantage_roll():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 > roll2:
		return roll1
	else:
		return roll2

def disadvantage_roll():
	roll1 = random.randint(1, 20)
	roll2 = random.randint(1, 20)
	if roll1 < roll2:
		return roll1
	else:
		return roll2

n = 1000000

print("DC\tNormal\tAdvantage\tDisadvantage")
for dc in range(5, 16, 5):
	normal = 0
	advantage = 0
	disadvantage = 0
	for i in range(n):
		if normal_roll() >= dc:
			normal += 1
		if advantage_roll() >= dc:
			advantage += 1
		if disadvantage_roll() >= dc:
			disadvantage += 1
	print(f"{dc}\t{normal/n:.3f}\t{advantage/n:.3f}\t\t{disadvantage/n:.3f}")
