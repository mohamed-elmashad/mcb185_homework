# authors: Mo, Aidan

import genomeutils
import mcb185
import sys

path = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])

for defline, seq in mcb185.read_fasta(path):
	print('>' + defline)
	seq_list = list(seq)
	for i in range(len(seq) - w + 1):
		s = seq[i:i + w]
		if genomeutils.entropy(s) < threshold:
			for j in range(i, i + w):
				seq_list[j] = 'N'
	masked_seq = ''.join(seq_list)
		
	genomeutils.pretty_print(masked_seq)

