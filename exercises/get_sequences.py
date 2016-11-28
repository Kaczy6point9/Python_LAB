def seq(name, name2):
	lines = []
	tuples = ()
	with open(name) as f:
		f.readline();
		for line in f:
			lines.append(line.strip())
	sequence = "".join(lines)
	with open(name2) as f:
		f2 = open("result.txt", 'w')
		for line in f:
			tuples = line.split()
			splited = sequence[int(tuples[1]):int(tuples[2])]
			f2.write(splited+ '\n')


seq("human.mito.genome.fasta", "human.mito.gene.positions.txt")
