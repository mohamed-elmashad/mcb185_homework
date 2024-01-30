# authors: Mo, Aidan

def hydropathy(amino_acid):
	if amino_acid == "A":
		return 1.80
	elif amino_acid == "C":
		return 2.50
	elif amino_acid == "D":
		return -3.50
	elif amino_acid == "E":
		return -3.50
	elif amino_acid == "F":
		return 2.80
	elif amino_acid == "G":
		return -0.40
	elif amino_acid == "H":
		return -3.20
	elif amino_acid == "I":
		return 4.50
	elif amino_acid == "K":
		return -3.90
	elif amino_acid == "L":
		return 3.80
	elif amino_acid == "M":
		return 1.90
	elif amino_acid == "N":
		return -3.50
	elif amino_acid == "P":
		return -1.60
	elif amino_acid == "Q":
		return -3.50
	elif amino_acid == "R":
		return -4.50
	elif amino_acid == "S":
		return -0.80
	elif amino_acid == "T":
		return -0.70
	elif amino_acid == "V":
		return 4.20
	elif amino_acid == "W":
		return -0.90
	elif amino_acid == "Y":
		return -1.30

# Test using assert
assert(hydropathy("A") == 1.80)
assert(hydropathy("P") == -1.60)
assert(hydropathy("W") == -0.90)
