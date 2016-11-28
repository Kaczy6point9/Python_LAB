from codon_table import codon_table

def translate(seq, codons = codon_table['standard'], frame = 1):
	start = frame - 1
	lenght = len(seq)
	proteins = "".join(codons[seq[i:i+3]] for i in range(start, lenght+1 , 3) if len(seq[i:i+3]) == 3)
	end = len(proteins) * 3
	return frame, start, end, proteins

print(translate("ACTATGCTTCTCCAATTTCCAATTTCCAATTCGTTTGCTTCATCAGCTCCCAAATTCTCCCGCTGACCCCTAAGTTCTACAAAATCCATGATCATCGTCGTTTAG",frame = 3))
