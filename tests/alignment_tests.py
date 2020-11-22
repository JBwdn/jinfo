import os
import sys
import unittest

# Explicit path modification to import jinfo from the higher level folder, from: docs.python-guide.org/writing/structure
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from jinfo.alignment import BaseAlignment


class TestBaseAlignment(unittest.TestCase):
    def setUp(self):
        return

    def test_obj_methods(self):
        return
