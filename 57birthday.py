# authors: Mo, Aidan

import random
import sys

trials = int(sys.argv[1])
days = int(sys.argv[2])
people = int(sys.argv[3])

dup = 0
propability = 0
bdays = []

# initialize and reset the list of bdays
for i in range(days):
	bdays.append(0)

for t in range(trials):
	# reset list of bdays
	for i in range(days):
		bdays[i] = 0

	# generate random bdays
	for i in range(people):
		bdays[random.randint(0, days-1)] += 1	
	
	# calculate the probability of duplicate bdays
	for count in bdays:
		if count > 1:
			dup += 1
			break

propability = dup / trials
print(propability)





