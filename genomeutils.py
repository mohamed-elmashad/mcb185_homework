import gzip
import math

def transcribe(dna):
	return dna.replace('T', 'U')

def reverse_complement(dna):
	rc = []
	for nt in dna[::-1]:
		if nt == 'A':
			rc.append('T')
		elif nt == 'T':
			rc.append('A')
		elif nt == 'C':
			rc.append('G')
		elif nt == 'G':
			rc.append('C')
		else:
			rc.append('N')
	return ''.join(rc)

def translate(dna):
	protein_sequence = ''
	for i in range(0, len(dna), 3):
		codon = dna[i:i+3]
		if codon in ['TTT', 'TTC']:
			protein_sequence += 'F'
		elif codon in ['TTA', 'TTG', 'CTT', 'CTC', 'CTA', 'CTG']:
			protein_sequence += 'L'
		elif codon in ['TCT', 'TCC', 'TCA', 'TCG']:
			protein_sequence += 'S'
		elif codon in ['TAT', 'TAC']:
			protein_sequence += 'Y'
		elif codon in ['TGT', 'TGC']:
			protein_sequence += 'C'
		elif codon == 'TGG':
			protein_sequence += 'W'
		elif codon in ['CCT', 'CCC', 'CCA', 'CCG']:
			protein_sequence += 'P'
		elif codon in ['CAT', 'CAC']:
			protein_sequence += 'H'
		elif codon in ['CAA', 'CAG']:
			protein_sequence += 'Q'
		elif codon in ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']:
			protein_sequence += 'R'
		elif codon in ['ATT', 'ATC', 'ATA']:
			protein_sequence += 'I'
		elif codon == 'ATG':
			protein_sequence += 'M'
		elif codon in ['ACT', 'ACC', 'ACA', 'ACG']:
			protein_sequence += 'T'
		elif codon in ['AAT', 'AAC']:
			protein_sequence += 'N'
		elif codon in ['AAA', 'AAG']:
			protein_sequence += 'K'
		elif codon in ['AGT', 'AGC']:
			protein_sequence += 'S'
		elif codon in ['AGA', 'AGG']:
			protein_sequence += 'R'
		elif codon in ['GTT', 'GTC', 'GTA', 'GTG']:
			protein_sequence += 'V'
		elif codon in ['GCT', 'GCC', 'GCA', 'GCG']:
			protein_sequence += 'A'
		elif codon in ['GAT', 'GAC']:
			protein_sequence += 'D'
		elif codon in ['GAA', 'GAG']:
			protein_sequence += 'E'
		elif codon in ['GGT', 'GGC', 'GGA', 'GGG']:
			protein_sequence += 'G'
		elif codon in ['TAA', 'TAG', 'TGA']:
			protein_sequence += '*'
		else:
			protein_sequence += 'X'  # if unknown codon, mark as 'X'
	return protein_sequence

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
	elif amino_acid == "U":
		return 2.50
	elif amino_acid == "V":
		return 4.20
	elif amino_acid == "W":
		return -0.90
	elif amino_acid == "Y":
		return -1.30

def average_hydropathy(sequence):
	total, num = 0, 0
	for aa in sequence:
		total += hydropathy(aa)
		num += 1
	return total / num
	
def gc_comp(seq):
	return (seq.count('C') + seq.count('G')) / len(seq)

def gc_comp_counts(count_c, count_g, seq_length):
	return (count_c + count_g) / seq_length

def gc_skew(seq):
	c = seq.count('C')
	g = seq.count('G')
	return gc_skew_counts(c, g)

def gc_skew_counts(c, g):
	if c + g == 0:
		return 0
	return (g - c) / (g + c)


def entropy(seq):
	A = seq.count('A')
	C = seq.count('C')
	G = seq.count('G')
	T = seq.count('T')
	return entropy_count(A, C, G, T)

def entropy_count(A, C, G, T):
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

def read_genome_sequence(file_path):
	genome = []
	with gzip.open(file_path, 'rt') as fp:
		for line in fp:
			if line.startswith('ORIGIN'):
				break
		for line in fp:
			words = line.upper().split()
			for word in words[1:]:
				genome.append(word)
	return ''.join(genome)

def print_pwm(name, identifier, description, pwm):
	print('AC', name)
	print('XX')
	print('ID', identifier)
	print('XX')
	print('DE', description)
	print('PO\tA\tC\tG\tT')
	for i, count in enumerate(pwm):
		a_count = count['A']
		c_count = count['C']
		g_count = count['G']
		t_count = count['T']
		print(f'{i+1:<8}{a_count:<8}{c_count:<8}{g_count:<8}{t_count:<8}')
	print('XX')
	print('//')

def read_gff(gff_file, wanted_feature):
	features = []
	with gzip.open(gff_file, 'rt') as fp:
		for line in fp:
			fields = line.split('\t')

			ID = fields[0]
			feature_source = fields[1]
			feature_type = fields[2]
			start = int(fields[3]) - 1
			end = int(fields[4]) - 1
			score = fields[5]
			strand = fields[6]
			info = fields[7]

			if feature_source == wanted_feature and score != '.' or \
				(wanted_feature == 'all'):
				feature_data = (ID, feature_source, feature_type, start, end, score, 
						strand, info)
				features.append(feature_data)
	return features

def read_vcf(vcf_file):
	variants = []
	with gzip.open(vcf_file, 'rt') as fp:
		for line in fp:				
			fields = line.split('\t')
			chromosome = fields[0]
			position = int(fields[1])
			ID = fields[2]
			ref = fields[3]
			alt = fields[4]

			variant_data = (chromosome, position, ID, ref, alt)
			variants.append(variant_data)
	return variants

def pretty_print(seq):
	for i in range(0, len(seq), 60):
		print(seq[i:i+60])
