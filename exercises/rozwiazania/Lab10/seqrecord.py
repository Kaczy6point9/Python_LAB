class SeqRecord:
    
    def __init__(self, id, sequence, description=None):
        self.id = id
        self.seq = sequence
        self.description = description

    def set_description(self, new_description):
        self.description = new_description

    def display(self):
        f = 'ID      :  '+self.id + '\n'
        if self.description:
            f += 'DESC  :'+self.description + '\n'
        f += 'SEQ   :'+self.seq
        return f

    def __str__(self):
        return self.display()
   
    def __len__(self):
        return len(self.seq)

    def __contains__(self, char):
        return char in self.seq

    def __iter__(self):
        return iter(self.seq)


class DNARecord(SeqRecord):
    
    def transcribe(self):
        return self.seq.replace('T', 'U')


s1 = DNARecord('gene1', 'ATG')
print(s1.transcribe())