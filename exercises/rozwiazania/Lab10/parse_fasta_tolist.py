def parse_fasta_tolist(filename):
	fasta = []
	seq_id = ''
	tmp_line = ''
	with open(filename, "r") as f:
		for line in f:
			line = line.strip()
			if line[0] == ">":
				if seq_id:
					my_tumple = (seq_id, desq, tmp_line)
					fasta.append(my_tumple)
					tmp_line = ' '
				splited_line = line.split()
				seq_id = splited_line[0]
				desq = " ".join(splited_line[1:])
				
			else:
				tmp_line += line

		my_tumple = (seq_id, desq, tmp_line)
		fasta.append(my_tumple)
		tmp_line = ' '
	return fasta


print(parse_fasta_tolist('cos.fasta'))
