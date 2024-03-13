#!/usr/bin/env python3
import argparse
import mcb185
import genomeutils

parser = argparse.ArgumentParser(description='DNA entropy filter.')
parser.add_argument('file', type=str, help='name of fasta file')
parser.add_argument('-s', '--size', type=int, default=20,
	help='window size [%(default)i]')
parser.add_argument('-e', '--entropy', type=float, default=1.4,
	help='entropy threshold [%(default).3f]')
parser.add_argument('--lower', action='store_true', help='soft mask')
arg = parser.parse_args()

path = arg.file
w = arg.size
threshold = arg.entropy

for defline, seq in mcb185.read_fasta(path):
	print('>' + defline)
	seq_list = list(seq)
	for i in range(len(seq) - w + 1):
		s = seq[i:i + w]
		if genomeutils.entropy(s) < threshold:
			for j in range(i, i + w):
				if arg.lower:
					seq_list[j] = seq_list[j].lower()
				else:
					seq_list[j] = 'N'
	masked_seq = ''.join(seq_list)

	genomeutils.pretty_print(masked_seq)
