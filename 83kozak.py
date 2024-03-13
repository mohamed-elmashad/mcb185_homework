import gzip
import mcb185
import sys
import genomeutils

def count_kozak_sequences(genome_seq, file_path):
	kozaks = []
	k_length = 14
	for i in range(k_length):
		kozaks.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

	with gzip.open(file_path, 'rt') as fp:
		for line in fp:
			fields = line.split()
			if fields[0] != 'CDS' or 'join' in fields[1]:
				continue

			if 'complement' in fields[1]:
				start_index = fields[1].index('(')
				end_index = fields[1].index(')')
				coordinates = fields[1][start_index:end_index]
				idx = int(coordinates.split('..')[1])
				k_seq = mcb185.anti_seq(genome_seq[idx-5:idx+9])
			else:
				coordinates = fields[1]
				idx = int(coordinates.split('..')[0])
				k_seq = genome_seq[idx-10:idx+4]

			for i, nt in enumerate(k_seq):
				kozaks[i][nt] += 1

	return kozaks

genome_file = sys.argv[1]
genome_sequence = genomeutils.read_genome_sequence(genome_file)
kozak_counts = count_kozak_sequences(genome_sequence, genome_file)
genomeutils.print_pwm('IMTSU001', 'ECKOZ', 'E. coli Kozak sequence', 
						kozak_counts)
