# authors: Mo, Aidan

alphabet = 'ACGT'
match = '+1'
mismatch = '-1'

# Print header
print('   ', end='')
for i in alphabet:
	print(i, end='  ')
print('')

for i in alphabet:
	print(i, end=' ')
	for j in alphabet:
		if i == j:
			print('+1', end=' ')
		else:
			print('-1', end=' ')
	print('')