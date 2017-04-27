import entities
import unittest
class LocalizacaoGeograficaTest(unittest.TestCase):
    
    
    def setUp(self):
        self.locGeo = entities.LocalizacaoGeografica(1111, 1111)
    
    def test_get_latitude(self):
        self.assertEqual(self.locGeo._get_latitude(), 1111);
    
    def test_get_longitude(self):
        self.assertEqual(self.locGeo._get_longitude(), 1111);
        
    def tearDown(self):
        print("fechando arquivos")



if __name__ == "__main__":
    unittest.main()
