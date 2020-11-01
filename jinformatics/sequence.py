import primer3

class WrongSequenceType(Exception):
    """
    Error for creating a sequence of the wrong type based on its bases
    """
    pass


class BaseSequence:
    """
    Base class for Sequence objects
    """
    def __init__(self, sequence: str):
        self.seq = sequence
        self.len = len(sequence)
        return


class NucSequence(BaseSequence):
    """
    Base class for nucleotide sequences
    """
    def tm(self):
        return


class DNASequence(NucSequence):
    """
    Class to hold sequences of DNA
    """
    def transcribe(self):
        return

    def translate(self):
        return

    def reverse_complement():
        return

    def MW():
        return


class RNASequence(NucSequence):
    """
    Class to hold RNA sequences
    """
    def reverse_transcribe():
        return

    def translate():
        return


class AASequence(BaseSequence):
    """
    Class to hold amino acid sequences
    """
    def MW(self):
        return


if __name__ == "__main__":
    pass
