import sys
import mcb185

# for defline, seq in mcb185.read_fasta(sys.argv[1]):
# 	print(defline[:30],seq[:40], len(seq))

# for defline, seq in mcb185.read_fasta(sys.argv[1]):
# 	defwords = defline.split()
# 	name = defwords[0]
# 	gc = 0
# 	for nt in seq:
# 		if nt == 'C' or nt == 'G': gc += 1
# 	print(name, gc/len(seq))

# nts = 'ACGTN' # should really be defined outside the loop
# counts = []
# for i in range(len(nts)): counts.append(0)
# for nt in seq:
# 	if   nt == 'A': counts[0] += 1
# 	elif nt == 'C': counts[1] += 1
# 	elif nt == 'G': counts[2] += 1
# 	elif nt == 'T': counts[3] += 1
# 	else: counts[4] += 1
# print(name, end='\t')
# for n in counts: print(f'{n/len(seq):.4f}', end='\t')
# print()