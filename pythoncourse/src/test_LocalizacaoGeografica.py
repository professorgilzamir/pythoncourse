import entities
import unittest
class LocalizacaoGeograficaTest(unittest.TestCase):
    def test_get_latitude(self):
        locGeo = entities.LocalizacaoGeografica(1111, 1111)
        self.assertEqual(locGeo._get_latitude(), 1111);
