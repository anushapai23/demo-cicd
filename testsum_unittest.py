# testsum_unittest.py

import unittest
from testsum import sum


class TestSum(unittest.TestCase):
	def test_int_1_2(self):
		self.assertEqual(3,sum(1,2))
	def test_str_1_2(self):
		self.assertEqual("12",sum("1","2"))

if __name__=='__main__':
	unittest.main()