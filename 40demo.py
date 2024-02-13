import random

for i in range(5):
	print(random.random())

for i in range(51):
	print(random.choice("AGCT"), end="")
print()

for i in range(200):
	r = random.random()
	if r < 0.7: print(random.choice("AT"), end="")
	else: print(random.choice("GC"), end="")
print()

print(10, 20, 30, 40, sep='\t')
i = 1
pi = 3.14159
print(f'formatted string {i} {pi}')
print(f'tau {pi + pi}')

random.seed(1)
print(random.random())
print(random.random())
random.seed(2)
print(random.random())
print(random.random())
random.seed(1)
print(random.random())
print(random.random())

games = 10
for i in range(games):
	print(f'game #{i}')
	for target in range(2, 13):
		d1 = random.randint(1, 6)
		d2 = random.randint(1, 6)
		if d1 + d2 == target:
			print(f'yay, rolled {d1} and {d2} for {target} points')