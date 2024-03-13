# authors: Mo, Aidan

import genomeutils
import mcb185
import sys

def six_frame_translation(dna):
	frames = []
	reverse = genomeutils.reverse_complement(dna)
	for i in range(3):
		frames.append(genomeutils.translate(dna[i:]))
		frames.append(genomeutils.translate(reverse[i:]))
	return "".join(frames)

def find_putative_genes(dna_sequences_file, protein_length):
	protein_deflines = []
	protein_sequences = []
	for defline, sequence in mcb185.read_fasta(dna_sequences_file):
		translated_frame = six_frame_translation(sequence)

		segments = translated_frame.split('*')
		for s in segments:
			start_index = s.find('M')
			if start_index != -1:
				protein = s[start_index:]
				if len(protein) >= protein_length:
					protein_deflines.append(defline)
					protein_sequences.append(protein)

		for i in range(len(protein_deflines)):
			print(f'>{protein_deflines[i]}')
			print(protein_sequences[i])
		print(f'Found {len(protein_deflines)} putative genes')

path = sys.argv[1]
protein_length = int(sys.argv[2])

# ensure protein length is at least 100
if protein_length < 100:
	sys.exit("Protein length must be at least 100")

find_putative_genes(path, protein_length)