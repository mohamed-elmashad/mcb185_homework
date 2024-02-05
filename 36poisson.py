# authors: Mo, Aidan

import math

def poisson(n, k):
	print(n**k * math.e**-n / math.factorial(k))

poisson(5, 3)
poisson(3, 6)
poisson(5, 31)


