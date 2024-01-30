# authors: Mo, Aidan

def oligotemp(A, C, G, T):
	length = A + C + G + T

	if length <= 13:
		return(A + T) * 2 + (G + C) * 4
	else:
		return(64.9 + 41 * (G + C - 16.4) / (length))

print("A = 4, C = 3, G = 2, T = 1")
print(oligotemp(4, 3, 2, 1))

print("A = 13, C = 3, G = 32, T = 19")
print(oligotemp(13, 3, 32, 19))

print("A = 19, C = 13, G = 5, T = 12")
print(oligotemp(19, 13, 5, 12))

