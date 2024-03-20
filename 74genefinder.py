import genomeutils
import mcb185
import sys

def find_ORFS(sequence, positive):
	symbol = ""
	if positive: 
		symbol = '+'
	else:
		symbol = '-'
	orfs = []

	# check all three reading frames
	for frame in range(3):
		# iterate over each nucleotide in the frame
		for i in range(frame, len(sequence)-2, 3):
			if sequence[i:i + 3] == 'ATG':
				for j in range(i + 3, len(sequence)-2, 3):
					if sequence[j:j + 3] in ('TAA', 'TAG', 'TGA'):
						start = i + 1
						end = j + 3
						overlap = False
						for o in orfs:
							existing_start = o[0]
							existing_end = o[1]
							if (start <= existing_end and start >= existing_start) or \
								(end <= existing_end and end >= existing_start):
								overlap = True
								break
						if not overlap:
							orfs.append((start, end, symbol))
						break
	return orfs

def find_cds(sequence, min_orf_length):
	cds_list = []
	# Positive strand
	orfs = find_ORFS(sequence, True)
	for orf in orfs:
		start, end, strand = orf
		if end - start >= min_orf_length:
			cds_list.append(orf)

	# Negative strand
	orfs = find_ORFS(genomeutils.reverse_complement(sequence), False)
	for orf in orfs:
		start, end, strand = orf
		if end - start >= min_orf_length:
			cds_list.append((len(sequence)-end + 1, len(sequence)-end + 1, '-'))

	return cds_list

fasta_file = sys.argv[1]
min_orf_length = int(sys.argv[2])
for defline, sequence in mcb185.read_fasta(fasta_file):
	cds_list = find_cds(sequence, min_orf_length)
	for idx, (start, end, strand) in enumerate(cds_list, start=1):
		print(f"{defline}\tGeneFinder\tCDS\t{start}\t"
			f"{end}\t.\t{strand}\t.\tID=CDS{idx}")
