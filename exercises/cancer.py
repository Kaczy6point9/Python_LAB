def zbior(name):
	zbior = set()
	with open(name) as f:
		for line in f:
			zbior.add(line.strip())
	return zbior

def common():
	c1 = zbior("cancer1.txt")
	c2 = zbior("cancer2.txt")
	c = zbior("control.txt")
	common = (c1&c2)-c
	f = open("common_gene.txt", 'w')
	for z in common:
		f.write(z+'\n')
	f.close

common()
