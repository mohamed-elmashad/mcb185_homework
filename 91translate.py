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
	protein_seq = genomeutils.translate(seq)
	# find first methionine
	start_index = protein_seq.find('M')
	if start_index != -1:
		protein_seq_trimmed = protein_seq[start_index:]
		# trim off stop codon
		end_index = protein_seq_trimmed.find('*')
		protein_seq_trimmed = protein_seq_trimmed[:end_index]
		if len(protein_seq_trimmed) >= args.min:
			if not args.anti:
				print('>' + name)
				genomeutils.pretty_print(protein_seq_trimmed)
			else:
				print('>' + name + ' (strand)')
				genomeutils.pretty_print(protein_seq_trimmed)

				print('>' + name + ' (anti-parallel strand)')
				translated_seq = genomeutils.translate(genomeutils.reverse_complement(seq))
				genomeutils.pretty_print(translated_seq[start_index:])
