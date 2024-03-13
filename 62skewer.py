# authors: Mo, Aidan

import genomeutils
import mcb185
import sys

def efficient_skew(seq, w):
	c_count = 0
	g_count = 0
	for i in range(len(seq) - w + 1):
		s = seq[i:i + w]
		if i == 0:
			c_count = s.count('C')
			g_count = s.count('G')
		else:
			# decrement c and g if they are removed from previous window
			if seq[i - 1] == 'C':
				c_count -= 1
			if seq[i - 1] == 'G':
				g_count -= 1
			# increment c and g if they are added in next window
			if seq[i + w - 1] == 'C':
				c_count += 1
			if seq[i + w - 1] == 'G':
				g_count += 1
			
		print(f'{i}\t{genomeutils.gc_comp_counts(c_count, g_count, w):.3f}', end='')
		print(f'\t{genomeutils.gc_skew_counts(c_count, g_count):.3f}')

if len(sys.argv) > 1:
	path = sys.argv[1]
	w = int(sys.argv[2])
	for defline, s in mcb185.read_fasta(sys.argv[1]):
		efficient_skew(s, w)	
else:
	seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
	w = 10
	efficient_skew(seq, w)



