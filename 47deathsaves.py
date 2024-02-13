# authors: Mo, Aidan

import random

def roll():
	return random.randint(1, 20)

n = 1000000
deaths = 0
stable = 0
revived = 0

for i in range(n):
	failures = 0
	successes = 0
	while True:
		r = roll()
		if r == 1:
			failures += 2
		elif r == 20:
			revived += 1
			break
		elif r < 10:
			failures += 1
		else:
			successes += 1
			
		if failures >= 3:
			deaths += 1
			break
		if successes >= 3:
			stable += 1
			break
			
print("deaths:", deaths, "average", deaths/n)
print("stable:", stable, "average", stable/n)
print("revived:", revived, "average", revived/n)
