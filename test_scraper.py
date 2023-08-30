import unittest
from scraper import Scraper

class Scraper_test(unittest.TestCase):
    def setUp(self):
        print('setUp')
        self.asin1 = Scraper("B09713NW8H")
        self.asin2 = Scraper("B07CSQ5VJP")
        
    def test_get_pl_soup(self):
        print('get_pl_soup')
        
        self.assertNotEqual(self.asin1.get_de_soup(), '')
        self.assertNotEqual(self.asin2.get_de_soup(), '')

        
    def test_get_de_soup(self):
        print('get_de_soup')
        self.assertNotEqual(self.asin1.get_de_soup(), '')
        self.assertNotEqual(self.asin2.get_de_soup(), '')
        
    def test_get_get_fr_soup(self):
        print('get_fr_soup')
        self.assertNotEqual(self.asin1.get_fr_soup(), '')
        self.assertNotEqual(self.asin2.get_fr_soup(), '')
        
    def test_get_description(self):
        print('get_description')

        self.assertNotEqual(self.asin1.get_pl_soup(), '')
        self.assertNotEqual(self.asin2.get_de_soup(), '')
        
    def test_scrap_technical_spec(self):
        print('scrap_technical_spec')

        self.assertNotEqual(self.asin1.scrap_technical_spec(self.asin1.get_pl_soup()), "Zobacz dormatowanie strony (a-row a-spacing-top-base)")
        self.assertNotEqual(self.asin2.scrap_technical_spec(self.asin2.get_de_soup()), "Zobacz dormatowanie strony (a-row a-spacing-top-base)")
        
    def test_scrap_front_table(self):
        print('scrap_front_table')

        self.assertNotEqual(self.asin1.scrap_front_table(self.asin1.get_pl_soup()), "Nie udało się pobrać tablicy frontowej, sprawdz id(feature-bullets)")
        self.assertNotEqual(self.asin2.scrap_front_table(self.asin2.get_de_soup()), "Nie udało się pobrać tablicy frontowej, sprawdz id(feature-bullets)")
   
   
   
if __name__ == '__main__':
    unittest.main()
