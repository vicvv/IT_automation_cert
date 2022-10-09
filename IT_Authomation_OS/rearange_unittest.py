import unittest

from rearange import rearrange_name

class TestRearange(unittest.TestCase):
    def test_basic(self):
        case = "Lovley, Ada"
        expected = "Ada, Lovley"
        self.assertEqual(rearrange_name(case), expected)
        
    def test_empty(self):
        case =""
        expected =""
        self.assertEqual(rearrange_name(case), expected)
        
unittest.main()
        