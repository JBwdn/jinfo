class BaseSeq:
    """
    Base class for DNA/RNA/AA sequence objects
    """

    def __init__(self, sequence: str = ""):
        self.seq = sequence
        self.len = len(sequence)
        return

    def update_seq(self, sequence: str = ""):
        self.seq = sequence
        self.len = len(sequence)
        return


class NucSeq(BaseSeq):
    """
    Base class for nucleotide sequences
    """

    def tm(self):
        return


class DNASeq(NucSeq):
    """
    Class to hold sequences of DNA
    """

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


class RNASeq(NucSeq):
    """
    Class to hold RNA sequences
    """

    def reverse_transcribe(self):
        return

    def translate(self):
        return


class AASeq(BaseSeq):
    """
    Class to hold amino acid sequences
    """

    def MW(self):
        return


if __name__ == "__main__":
    pass
