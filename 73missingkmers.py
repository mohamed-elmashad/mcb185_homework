import sys
import mcb185
import genomeutils
import itertools

k = 1
found_missing = False

while not found_missing:
	kcount = {}
	for defline, seq in mcb185.read_fasta(sys.argv[1]):
		for s in [seq, genomeutils.reverse_complement(seq)]:
			for i in range(len(s) - k + 1):
				kmer = s[i:i+k]
				if kmer not in kcount:
					kcount[kmer] = 0
				kcount[kmer] += 1
	
	missing_kmers = []
	bases = ['A', 'C', 'G', 'T']

	for kmer in itertools.product(bases, repeat=k):
		kmer = ''.join(kmer)
		if kmer not in kcount:
			missing_kmers.append(kmer)

	if missing_kmers:
		found_missing = True
		print("Missing k-mers at k =", k)
		print("number of missing k-mers:", len(missing_kmers))
	else:
		k += 1