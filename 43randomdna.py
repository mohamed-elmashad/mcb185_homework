# authors: Mo, Aidan

import random

seq_name = ">seq-"
seq_len = 50
n = 100

seq_letters = "ACGT"

for i in range(n):
	print(f'{seq_name}{i+1}')
	for letter in range(seq_len):
		print(random.choice(seq_letters), end='')
	print()