DNA_VOCAB = {"A", "T", "C", "G", "X"}
RNA_VOCAB = {"A", "U", "C", "G", "X"}
AA_VOCAB = {
    "G",
    "A",
    "L",
    "M",
    "F",
    "W",
    "K",
    "L",
    "Q",
    "E",
    "S",
    "P",
    "V",
    "I",
    "C",
    "Y",
    "H",
    "R",
    "N",
    "D",
    "T",
}


class SeqVocabError(Exception):
    pass


class BaseSeq:
    """
    Parent class for DNA/RNA/AA sequence objects
    """

    def __init__(self, sequence: str = "", vocab: set = None):
        self.vocab = vocab
        self.update_seq(sequence)
        self.len = len(self.seq)
        return

    def check_seq_valid(self):
        """
        Ensure that the sequence string is consistant with the vocab
        """
        if self.vocab is not None:
            if not self.vocab.issuperset(set(self.new_seq)):
                raise SeqVocabError("")
        return

    def update_seq(self, sequence: str = ""):
        """
        Replace the sequence string with a new string
        """
        self.new_seq = sequence
        self.check_seq_valid()
        self.seq = sequence
        self.len = len(sequence)
        return


class DNASeq(BaseSeq):
    """
    Class to hold sequences of DNA
    """

    def __init__(self, sequence: str = ""):
        """
        Call the superclass constructor with new default vocab argument
        """
        super(DNASeq, self).__init__(sequence=sequence, vocab=DNA_VOCAB)
        return

    def transcribe(self):
        return

    def translate(self):
        return

    def reverse_complement(self):
        return

    def MW(self):
        return

    def GC(self):
        return

    def tm(self):
        return


class RNASeq(BaseSeq):
    """
    Class to hold RNA sequences
    """

    def __init__(self, sequence: str = ""):
        """
        Call the superclass constructor with new default vocab argument
        """
        super(RNASeq, self).__init__(sequence=sequence, vocab=RNA_VOCAB)
        return

    def reverse_transcribe(self):
        return

    def translate(self):
        return


class AASeq(BaseSeq):
    """
    Class to hold amino acid sequences
    """

    def __init__(self, sequence: str = ""):
        """
        Call the superclass constructor with new default vocab argument
        """
        super(AASeq, self).__init__(sequence=sequence, vocab=AA_VOCAB)
        return

    def MW(self):
        return


if __name__ == "__main__":
    pass
