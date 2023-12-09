import city_function2 as cf2
import unittest

class TestCities(unittest.TestCase):
       
    def test_city_country(self):
        formatted_result = cf2.format_city_country('Montreal', 'Canada')
        self.assertEqual(formatted_result, 'Montreal, Canada')

    def test_city_country_population(self):
        formatted_result = cf2.format_city_country('Montreal', 'Canada', population=50000)
        self.assertEqual(formatted_result, 'Montreal, Canada - population 50000')  # Updated case


if __name__ == '__main__':
    unittest.main()
