import genomeutils
import sys
import mcb185

seq = ""
if len(sys.argv) > 1:
	path = sys.argv[1]
	for defline, s in mcb185.read_fasta(sys.argv[1]):
		seq += s
	w = int(sys.argv[2])
else:
	seq = 'ACGTACGTGGGGGACGTACGTCCCCC'
	w = 10

for i in range(len(seq) - w + 1):
	s = seq[i:i + w]
	print(f'{i}\t{genomeutils.gc_comp(s):.3f}\t{genomeutils.gc_skew(s):.3f}')