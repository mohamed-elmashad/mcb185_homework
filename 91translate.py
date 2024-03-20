#!/usr/bin/env python3
import argparse
import mcb185
import genomeutils

parser = argparse.ArgumentParser(description='mRNA translator.')
parser.add_argument('file', help='fasta file of mRNAs')
parser.add_argument('-m', '--min', type=int, default=100,
					help='minimum protein length [100]')
parser.add_argument('-a', '--anti', action='store_true',
					help='also examine the anti-parallel strand')
args = parser.parse_args()

for name, seq in mcb185.read_fasta(args.file):
	if not args.anti:
		protein_seq = genomeutils.translate(seq)
	else:
		reverse = genomeutils.reverse_complement(seq)
		protein_seq = genomeutils.translate(reverse)
		
	# find first methionine
	start_index = protein_seq.find('M')
	if start_index != -1:
		protein_seq_trimmed = protein_seq[start_index:]
		# trim off stop codon
		end_index = protein_seq_trimmed.find('*')
		protein_seq_trimmed = protein_seq_trimmed[:end_index]
		if len(protein_seq_trimmed) >= args.min:
			print('>' + name)
			genomeutils.pretty_print(protein_seq_trimmed)
