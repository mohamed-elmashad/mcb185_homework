# authors: Mo, Aidan

import gzip
import sys

def read_gff(gff_file, feature):
	lengths = []
	with gzip.open(gff_file, 'rt') as f:
		for line in f:
			if line[0] != '#':
				words = line.split()
				feature_type = words[2]
				if feature_type == feature:
					start, end = int(words[3]), int(words[4])
					lengths.append(end - start + 1)
	return lengths

# helper functions
def mean(lengths):
	total = 0
	for l in lengths:
		total += l
	return total / len(lengths)

def min_max(lengths):
	minimum = lengths[0]
	maximum = lengths[0]
	for l in lengths:
		if l < minimum:
			minimum = l
		if l > maximum:
			maximum = l
	return minimum, maximum

def median(lengths):
	lengths.sort()
	mid = len(lengths) // 2
	if len(lengths) % 2 == 0:
		return (lengths[mid - 1] + lengths[mid]) / 2
	else:
		return lengths[mid]

def std_dev(lengths):
	m = mean(lengths)
	total = 0
	for l in lengths:
		total += (l - m) ** 2
	return (total / len(lengths)) ** 0.5

def calculate_statistics(lengths):
	count = len(lengths)
	minimum, maximum = min_max(lengths)
	avg = mean(lengths)
	stddev = std_dev(lengths)
	med = median(lengths)
	return int(count), int(minimum), int(maximum), int(avg), int(stddev), int(med)

gffpath = sys.argv[1]
feature = sys.argv[2]

lengths = read_gff(gffpath, feature)

if len(lengths) == 0:
	sys.exit('No features found for ' + feature)

count, minimum, maximum, mean, std_dev, median = calculate_statistics(lengths)

print(f'Count: {count} \nMin: {minimum} \nMax: {maximum}')
print(f'Mean: {mean} \nStd_dev: {std_dev} \nMedian: {median}')
