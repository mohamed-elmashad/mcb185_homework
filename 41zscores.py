# authors: Mo, Aidan

import random

z1 = 0
z2 = 0
z3 = 0

limit = 100000

for i in range(limit):
	x = random.gauss(0, 1)
	if x > 1:
		z1 += 1
	elif x > 2:
		z2 += 1
	elif x > 3:
		z3 += 1

print(1 - 2*z1/limit)
print(1 - 2*z2/limit)
print(1 - 2*z3/limit)