# authors: Mo, Aidan

import sys

colorfile = sys.argv[1]
R = int(sys.argv[2])
G = int(sys.argv[3])
B = int(sys.argv[4])

def dtc(P, Q):
	d = 0
	for p, q in zip(P, Q):
		d += abs(int(p) - int(q))
	return d

def read_colors(colorfile):
	colors = list()
	for line in open(colorfile):
		name = line.split()[0]
		rgb = line.split()[2]
		R, G, B = rgb.split(',')
		t = (name, R, G, B) # Tuple
		colors.append(t)
	return colors

def closest(colors, R, G, B):
	closest_dist = 100000000
	for name, r, g, b in colors:
		d = dtc((R, G, B), (r, g, b))
		if d < closest_dist:
			closest = name
			closest_dist = d
	return closest

colors = read_colors(colorfile)
name = closest(colors, R, G, B)
print('closest color is: ', name)