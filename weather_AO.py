import sys
import requests
import json

icons_dict = {
    'Sunny': '☀️',
    'Cloudy': '☁️',
    'Partly cloudy': '⛅',
    'Rainy': '🌧️',
    'Stormy': '⛈️',
    'Snowy': '❄️'
}


def get_weather_data(city, api_key):
    url = "https://weatherapi-com.p.rapidapi.com/current.json"
    querystring = {"q": city}
    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "weatherapi-com.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    print(data)

    return data


def get_condition(weather_data):
    return weather_data['current']['condition']['text']


def get_temperature(weather_data):
    return weather_data['current']['temp_c']


def get_long_lat(weather_data):
    return weather_data['location']['lon'], weather_data['location']['lat']


def get_local_time(weather_data):
    return weather_data['location']['localtime']


def get_country(weather_data):
    return weather_data['location']['country']


def print_city_info(city, country):
    print(city, ",", country)


def print_weather_info(condition, temp_celsius, temp_faren, long, lat, local_time):
    cond_logo = icons_dict.get(condition, '🤔')  # not sure  icon if icon is not assigned in the icons dict
    temp_color = '\033[94m' if temp_celsius < 0 else '\033[91m' if temp_celsius > 30 else '\033[92m'
    print(f'\t{cond_logo}  {condition} \ttemp: {temp_color}{temp_celsius}℃\033[0m  / {temp_faren}℉ ')
    print(f'\tlongitude: {long} \tlatitude: {lat} \tlocal time: {local_time}')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Please provide a city name as a command line argument.')
    else:
        city = ' '.join(word for word in sys.argv[1:])
        api_key = '9bed24e805msh986358ba336fa52p107a58jsn86543b46e4c9'
        weather_data = get_weather_data(city, api_key)
        if 'error' in weather_data:
            print(weather_data['error'])
            print('Please enter a valid city name.')
        else:
            condition = get_condition(weather_data)
            temp_celsius = get_temperature(weather_data)
            temp_faren = round((temp_celsius * 9/5) + 32, 2)
            long, lat = get_long_lat(weather_data)
            local_time = get_local_time(weather_data)
            country = get_country(weather_data)

            print_city_info(city, country)
            print_weather_info(condition, temp_celsius, temp_faren, long, lat, local_time)



