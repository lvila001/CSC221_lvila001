import city_function as cf
import unittest

class TestCities(unittest.TestCase):
    
    def test_city_country(self):
        formatted_result = cf.format_city_country('Plattsburgh', 'US')
        self.assertEqual(formatted_result, "Plattsburgh, US")

if __name__ == '__main__':
    unittest.main()

