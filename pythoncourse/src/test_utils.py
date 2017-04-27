import utils 
import unittest

class UtilsTest(unittest.TestCase):
    def test_extract_filename(self):
        self.assertEqual(utils.extract_filename("/home/user/teste.txt.txt"), "/home/user/teste.txt")
        self.assertEqual(utils.extract_filename("/home/user/teste"), "/home/user/teste")
        self.assertEqual(utils.extract_filename("teste"), "teste")
        self.assertEqual(utils.extract_filename("teste.txt"), "teste")
        self.assertEqual(utils.extract_filename("teste.txt.txt"), "teste.txt")
        self.assertEqual(utils.extract_filename(".txt"), "")
        self.assertEqual(utils.extract_filename(""), "")
        self.assertEqual(utils.extract_filename(), None)
        
if __name__ == "__main__":
    unittest.main()