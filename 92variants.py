#!/usr/bin/env python3
import argparse
import genomeutils

parser = argparse.ArgumentParser(description='variant reporter')
parser.add_argument('gff', help='GFF file')
parser.add_argument('vcf', help='VCF file')
args = parser.parse_args()

def compare_variants_to_features(variants, features):
	combined_features = {}
	for variant in variants:
		for feature in features:
			# check if variant is within feature and has same chromosome
			if variant[0] == feature[0] and variant[1] >= feature[3] and \
				variant[1] <= feature[4]:
				position_key = (variant[0], variant[1])
				categories = feature[2]

				if position_key in combined_features:
					combined_features[position_key].add(categories)
				else:
					combined_features[position_key] = {categories}

	for position, categories in combined_features.items():
		categories_str = ','.join(sorted(categories))
		print(f"{position[0]}\t{position[1]}\t{categories_str}")

gff_features = genomeutils.read_gff(args.gff, 'all')  
vcf_variants = genomeutils.read_vcf(args.vcf)

compare_variants_to_features(vcf_variants, gff_features)
