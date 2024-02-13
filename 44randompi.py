# authors: Mo, Aidan

import random
import math

inside = 0
total = 0
while True:
	x = random.random()
	y = random.random()
	distance = math.sqrt(x*x + y*y)
	if distance < 1:
		inside += 1
	total += 1
	print(inside / total * 4)

