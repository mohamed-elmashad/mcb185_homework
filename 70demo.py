aas = 'IVLFCMAGTSWYPHEQDNKR'
kds = (4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, 
		-3.5, -3.5, -3.5, -3.5, -3.9, -4.5, 0)

def kd_list(seq):
	kd = 0
	for aa in seq:
		idx = aas.find(aa)
		kd += kds[idx]
	return kd/len(seq)
