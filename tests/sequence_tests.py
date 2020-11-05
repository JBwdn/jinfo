import os
import sys
import unittest

# Explicit path modification to import jinfo from the higher level folder, from: docs.python-guide.org/writing/structure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from jinfo.sequence import (
    BaseSeq,
    DNASeq,
    RNASeq,
    AASeq,
    SeqVocabError,
    UnknownBaseError,
    SeqLengthError,
)


class TestBaseSeq(unittest.TestCase):
    def setUp(self):
        # Create test data and BaseSeq object:
        self.test_label = "novocab"
        self.test_label2 = "novocab2"
        self.test_seq = "test sequence with no vocab"
        self.test_seq2 = "test sequence with no vocab2"
        self.base_obj = BaseSeq(self.test_seq, self.test_label)
        return

    def test_obj_methods(self):
        # Test constructor:
        self.assertEqual(self.base_obj.label, self.test_label)
        self.assertNotEqual(self.base_obj.seq, self.test_seq)
        self.assertEqual(self.base_obj.seq, self.test_seq.upper())
        self.assertEqual(self.base_obj.len, len(self.test_seq))

        # Test BaseSeq.update_label:
        self.base_obj.update_label(self.test_label2)
        self.assertEqual(self.base_obj.label, self.test_label2)

        # Test BaseSeq.update_seq:
        self.base_obj.update_seq(self.test_seq2)
        self.assertEqual(self.base_obj.seq, self.test_seq2.upper())
        self.assertEqual(self.base_obj.len, len(self.test_seq2))

        # Test BaseSeq.identity:
        value = self.base_obj.identity(BaseSeq(self.test_seq))
        self.assertEqual(value, 98.18)

        # Test BaseSeq.align:
        # Test BaseSeq.save_fasta:
        return


class TestDNASeq(unittest.TestCase):
    def setUp(self):
        # Create test data and DNASeq object:
        self.test_label = "test_DNASeq"
        self.test_seq = "AAAACCCCGGGGTTTT"
        self.test_seq_RNA = "AAAACCCCGGGGUUUU"
        self.dna_obj = DNASeq(self.test_seq, self.test_label)
        return

    def test_obj_methods(self):
        # Test Constructor:
        self.assertEqual(self.dna_obj.seq, self.test_seq)
        self.assertEqual(self.dna_obj.label, self.test_label)
        self.assertEqual(self.dna_obj.len, len(self.test_seq))

        # Test DNASeq vocab:
        self.assertRaises(SeqVocabError, self.dna_obj.update_seq, "4")
        self.assertRaises(SeqVocabError, self.dna_obj.update_seq, "!")
        self.assertRaises(SeqVocabError, self.dna_obj.update_seq, "O")

        # Test DNASeq.transcribe:
        self.assertEqual(self.dna_obj.transcribe(), self.test_seq_RNA)

        # Test DNASeq.translate:
        self.assertRaises(SeqLengthError, self.dna_obj.translate)
        self.dna_obj.update_seq("gtgataataaataacagaaat")
        self.assertEqual(self.dna_obj.translate(), "VIINNRN")

        # Test DNASeq.reverse_complement:
        self.assertEqual(self.dna_obj.reverse_complement(), "ATTTCTGTTATTTATTATCAC")

        # Test DNASeq.GC:
        self.assertEqual(self.dna_obj.GC(), 19.05)

        # Test DNASeq.tm:
        self.assertEqual(self.dna_obj.tm(), 39.14)

        # Test DNASeq.one_hot:
        self.dna_obj.update_seq("atcg")
        self.assertEqual(sum(self.dna_obj.one_hot()), 4)

        # Test DNASeq.find_CDS:
        # Test DNASeq.MW:
        return


class TestRNASeq(unittest.TestCase):
    def setUp(self):
        # Create test data and RNASeq object:
        self.rna_obj = RNASeq()
        return

    def test_obj_methods(self):
        self.rna_obj.update_seq("AUGCA")
        self.assertEqual(self.rna_obj.seq, "AUGCA")
        self.assertEqual(self.rna_obj.reverse_transcribe(), "ATGCA")
        self.assertRaises(
            SeqLengthError, self.rna_obj.translate,
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
