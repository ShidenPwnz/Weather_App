import unittest
from weather_AO import *


class TestWeatherFunctions(unittest.TestCase):

    weather_data = {
        'location': {
            'country': 'United States',
            'lat': '37.7749',
            'localtime': '2023-03-22 12:34',
            'lon': '-122.4194',
        },
        'current': {
            'condition': {
                'text': 'Sunny'
            },
            'temp_c': 20.5,
        },
    }

    def test_get_condition(self):
        condition = get_condition(self.weather_data)
        self.assertEqual(condition, 'Sunny')

    def test_get_temperature(self):
        temperature = get_temperature(self.weather_data)
        self.assertEqual(temperature, 20.5)

    def test_get_long_lat(self):
        long, lat = get_long_lat(self.weather_data)
        self.assertEqual(long, '-122.4194')
        self.assertEqual(lat, '37.7749')

    def test_get_local_time(self):
        local_time = get_local_time(self.weather_data)
        self.assertEqual(local_time, '2023-03-22 12:34')

    def test_get_country(self):
        country = get_country(self.weather_data)
        self.assertEqual(country, 'United States')

    def test_get_weather_data_valid_city(self):
        city = 'New York'
        api_key = '9bed24e805msh986358ba336fa52p107a58jsn86543b46e4c9'
        result = get_weather_data(city, api_key)
        self.assertNotIn('error', result)


if __name__ == '__main__':
    unittest.main()


