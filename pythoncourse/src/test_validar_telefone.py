import unittest
import entities
import classes

class EnderecoTest(unittest.TestCase):
   
    def test_validarTelefone(self):
     end = classes.Endereco()
     self.assertFalse(end.validarTelefone("(88)96234675"))
     self.assertFalse(end.validarTelefone("(88)9623-4675"))
     self.assertFalse(end.validarTelefone("88996234675"))
     self.assertFalse(end.validarTelefone("(88996234675"))
     self.assertFalse(end.validarTelefone("88)99223322"))
     self.assertFalse(end.validarTelefone("(88)9 99223322"))
     self.assertFalse(end.validarTelefone("(88)99922-3322"))		
     self.assertTrue(end.validarTelefone("(88)99223322"))
     self.assertTrue(end.validarTelefone("(88)999223322"))
     self.assertTrue(end.validarTelefone("(88)9 9623-4675"))
     self.assertRaise(Exception,end.validarTelefone(None))
     self.assertRaise(NUmeroInvalido, end.validarTelefone,("888"))

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
    '''
    
if __name__ == "__main__":
       unittest.main()
