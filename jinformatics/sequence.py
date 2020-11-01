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
    "*",
}

codon_table = {
    "AUA": "I",
    "AUC": "I",
    "AUU": "I",
    "AUG": "M",
    "ACA": "T",
    "ACC": "T",
    "ACG": "T",
    "ACU": "T",
    "AAC": "N",
    "AAU": "N",
    "AAA": "K",
    "AAG": "K",
    "AGC": "S",
    "AGU": "S",
    "AGA": "R",
    "AGG": "R",
    "CUA": "L",
    "CUC": "L",
    "CUG": "L",
    "CUU": "L",
    "CCA": "P",
    "CCC": "P",
    "CCG": "P",
    "CCU": "P",
    "CAC": "H",
    "CAU": "H",
    "CAA": "Q",
    "CAG": "Q",
    "CGA": "R",
    "CGC": "R",
    "CGG": "R",
    "CGU": "R",
    "GUA": "V",
    "GUC": "V",
    "GUG": "V",
    "GUU": "V",
    "GCA": "A",
    "GCC": "A",
    "GCG": "A",
    "GCU": "A",
    "GAC": "D",
    "GAU": "D",
    "GAA": "E",
    "GAG": "E",
    "GGA": "G",
    "GGC": "G",
    "GGG": "G",
    "GGU": "G",
    "UCA": "S",
    "UCC": "S",
    "UCG": "S",
    "UCU": "S",
    "UUC": "F",
    "UUU": "F",
    "UUA": "L",
    "UUG": "L",
    "UAC": "Y",
    "UAU": "Y",
    "UAA": "*",
    "UAG": "*",
    "UGC": "C",
    "UGU": "C",
    "UGA": "*",
    "UGG": "W",
}


class SeqVocabError(Exception):
    pass


class SeqLengthError(Exception):
    pass


class BaseSeq:
    """
    Parent class for DNA/RNA/AA sequence objects
    """

    def __init__(self, sequence: str = "", vocab: set = None):
        self.vocab = vocab
        self.update_seq(sequence.upper())
        self.len = len(self.seq)
        return

    def check_seq_valid(self):
        """
        Ensure that the sequence string is consistant with the vocab
        """
        if self.vocab is not None:
            if not self.vocab.issuperset(set(self.new_seq)):
                raise SeqVocabError("Seq contains bases not in vocab")
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
        """
        Returns: the transcript of the DNA sequence
        """
        return self.seq.replace("T", "U")

    def translate(self):
        """
        Returns: the translated protein sequence of the DNA sequence
        """
        transcript = self.transcribe()
        if len(transcript) % 3 != 0:
            raise SeqLengthError("Seq cannot be split into codons, not a multiple of 3")
        codon_list = [transcript[i : i + 3] for i in range(0, len(transcript), 3)]
        return "".join([codon_table[codon] for codon in codon_list])

    def reverse_complement(self):
        return

    def find_CDS(self):
        return

    def MW(self):
        return

    def GC(self, dp: int = 2):
        """
        Calculate the %GC of the DNA sequence
        Optional arg to control precision
        Returns: GC percentage
        """
        return round((self.seq.count("C") + self.seq.count("G")) / self.len, dp)

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
