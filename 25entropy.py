# authors: Mo, Aidan
import math

def entropy(A, C, G, T):
	total = A + C + G + T

	if total == 0:
		return 0

	probability_a = A / total
	probability_c = C / total
	probability_g = G / total
	probability_t = T / total

	a = probability_a * math.log2(probability_a) if probability_a > 0 else 0
	c = probability_c * math.log2(probability_c) if probability_c > 0 else 0
	g = probability_g * math.log2(probability_g) if probability_g > 0 else 0
	t = probability_t * math.log2(probability_t) if probability_t > 0 else 0

	return -(a + c + g + t)

print("Nucleotide Counts: A = 2, C = 3, G = 1, T = 10")
print("Entropy:", entropy(2, 3, 1, 10))

print("Nucleotide Counts: A = 5, C = 0, G = 8, T = 2")
print("Entropy:", entropy(5, 0, 8, 2))

print("Nucleotide Counts: A = 15, C = 5, G = 20, T = 0")
print("Entropy:", entropy(15, 5, 20, 0))

print("Nucleotide Counts: A = 0, C = 0, G = 0, T = 0")
print("Entropy:", entropy(0, 0, 0, 0))