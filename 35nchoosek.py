# authors: Mo, Aidan

import math

def nchoosek(n, k):
	numerator = math.factorial(n)
	if n < k:
		print('n cannot be less than k')
	else:
		denominator = math.factorial(k) * math.factorial(n-k)
		print(numerator / denominator)

nchoosek(5, 3)
nchoosek(100, 6)
nchoosek(61, 22)