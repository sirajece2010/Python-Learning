import unittest
import calc
import os,sys

class TestCalc(unittest.TestCase):
    def setUp(self):
        print("Setup Section")

    def tearDown(self):
        print("CleanUp Section")

    def test_add(self):
        print('Test1')
        self.assertEqual(calc.add(50,50),100)

    @unittest.skipIf(sys.version.startswith('2.'),'Platform not suppoorted')
    def test_sub(self):
        print('Test2')
        self.assertEqual(calc.sub(15,5),10)

if __name__ == '__main__':
    unittest.main()