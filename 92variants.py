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
		variant_chromosome, variant_position = variant[0], variant[1]
		for feature in features:
			feature_chromosome = feature[0]
			categories = feature[2]
			feature_start, feature_end = feature[3], feature[4]

			same_chromosome = variant_chromosome == feature_chromosome
			within_feature = variant_position >= feature_start and \
				variant_position <= feature_end

			if same_chromosome and within_feature:
				position_key = (variant[0], variant[1])

				if position_key in combined_features:
					combined_features[position_key].add(categories)
				else:
					combined_features[position_key] = {categories}

	for position, categories in combined_features.items():
		categories_str = ','.join(sorted(categories))
		chromosome, start = position
		print(f"{chromosome}\t{start}\t{categories_str}")


gff_features = genomeutils.read_gff(args.gff, 'all')  
vcf_variants = genomeutils.read_vcf(args.vcf)

compare_variants_to_features(vcf_variants, gff_features)
