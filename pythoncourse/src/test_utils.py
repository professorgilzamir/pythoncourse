import utils 
import unittest
from src.utils import NomeDeArquivoInvalido

class UtilsTest(unittest.TestCase):
    '''
    def test_extract_filename(self):
        self.assertEqual(utils.extract_filename("/home/user/teste.txt.txt"), "/home/user/teste.txt")
        self.assertEqual(utils.extract_filename("/home/user/teste"), "/home/user/teste")
        self.assertEqual(utils.extract_filename("teste"), "teste")
        self.assertEqual(utils.extract_filename("teste.txt"), "teste")
        self.assertEqual(utils.extract_filename("teste.txt.txt"), "teste.txt")
        self.assertRaises(Exception, utils.extract_filename, (".txt"))
        self.assertRaises(Exception, utils.extract_filename, (""))
        self.assertRaises(Exception, utils.extract_filename, ())
    '''    
    def test_extract_filename(self):
        error = False
        try:
            utils.extract_filename(".txt")
            utils.extract_filename("")
            utils.extract_filename()
        except NomeDeArquivoInvalido:
            error = True
        
        if not error:
            self.fail("Chamada nao gerou erro, mas deveria")

if __name__ == "__main__":
    unittest.main()