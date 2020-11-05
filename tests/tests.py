import unittest
from jinfo.sequence import (
    DNASeq,
    RNASeq,
    AASeq,
    SeqVocabError,
    UnknownBaseError,
    SeqLengthError,
)


class TestDNASeq(unittest.TestCase):
    def setUp(self):
        self.dna_obj = DNASeq()
        return

    def test_obj_methods(self):
        self.dna_obj.update_seq("AAAACCCCGGGGTTTT")
        self.assertEqual(self.dna_obj.seq, "AAAACCCCGGGGTTTT")
        self.assertEqual(self.dna_obj.len, 16)
        self.assertEqual(self.dna_obj.transcribe(), "AAAACCCCGGGGUUUU")

        self.assertRaises(SeqVocabError, self.dna_obj.update_seq, "4")
        self.assertRaises(SeqVocabError, self.dna_obj.update_seq, "!")
        self.assertRaises(SeqVocabError, self.dna_obj.update_seq, "O")
        return


class TestRNASeq(unittest.TestCase):
    def setUp(self):
        self.rna_obj = RNASeq()
        return

    def test_obj_methods(self):
        self.rna_obj.update_seq("AUGCA")
        self.assertEqual(self.rna_obj.seq, "AUGCA")
        self.assertEqual(self.rna_obj.reverse_transcribe(), "ATGCA")
        self.assertRaises(
            SeqLengthError,
            self.rna_obj.translate,
        )
        self.rna_obj.update_seq("AUGCAU")

        self.assertRaises(SeqVocabError, self.rna_obj.update_seq, "4")
        self.assertRaises(SeqVocabError, self.rna_obj.update_seq, "!")
        self.assertRaises(SeqVocabError, self.rna_obj.update_seq, "O")
        return


class TestAASeq(unittest.TestCase):
    def setUp(self):
        return

    def test_obj_methods(self):
        return


if __name__ == "__main__":
    unittest.main()
