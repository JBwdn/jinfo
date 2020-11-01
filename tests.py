import unittest
from jinformatics.sequence import DNASeq


class TestDNASeq(unittest.TestCase):
    def setUp(self):
        self.dna_obj = DNASeq()

    def test_methods(self):
        self.dna_obj.update_seq("AAAA")
        self.assertEqual(self.dna_obj.seq, "AAAA", "Test DNASeq seq property")
        self.assertEqual(self.dna_obj.len, 4, "Test DNASeq len property")

        self.dna_obj.update_seq("ATATAT")
        self.assertEqual(self.dna_obj.seq, "ATATAT", "Test DNASeq update_seq method")
        self.assertEqual(self.dna_obj.transcribe(), None)


if __name__ == "__main__":
    unittest.main()
