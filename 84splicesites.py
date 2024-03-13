
import sys
import mcb185
import genomeutils

fasta_file = sys.argv[1]
gff_file = sys.argv[2]
wanted_feature = sys.argv[3]

# isolate organism name from fasta file
organism_file = fasta_file.split('/')[-1].split('.')
organism_name = '.'.join(organism_file[:2]).capitalize()

donor_pwm = []
for i in range(6):
	donor_pwm.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})
acceptor_pwm = []
for i in range(7):
	acceptor_pwm.append({'A': 0, 'C': 0, 'G': 0, 'T': 0})

chromosomes = {}
for defline, sequence in mcb185.read_fasta(fasta_file):
	c = defline.split()[0]
	chromosomes[c] = sequence

introns = genomeutils.read_gff(gff_file, wanted_feature)
for i in introns:
	ID, source, f_type, start, end, num, strand, info = i

	if strand == '+':
		intron_seq = chromosomes[ID][start:end + 1]
	else:
		intron_seq = mcb185.anti_seq(chromosomes[ID][start:end + 1])

	donor_seq = intron_seq[0:6]
	for i, nt in enumerate(donor_seq):
		donor_pwm[i][nt] += 1

	acceptor_seq = intron_seq[-7:]
	for i, nt in enumerate(acceptor_seq):
		acceptor_pwm[i][nt] += 1

genomeutils.print_pwm(organism_name, 'ACC', 'splice acceptor', acceptor_pwm)
genomeutils.print_pwm(organism_name, 'DON', 'splice donor', donor_pwm)
