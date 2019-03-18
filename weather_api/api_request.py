''' Making requests and fetching weather data '''
import requests


class ApiRequest():

    def __init__(self, city):
        self.city = city

    def to_celsius(self, temp):
        celsius = int((temp - 273.15))
        return celsius

    def get_data(self):
        ''' Returns dict with data for chosen city (name, temperature, 
            weather description and icon symbol). 
            If error returns message (str) '''
        try:
            city_request = requests.get('http://api.openweathermap.org'
                                        '/data/2.5/forecast?q={}&APPID='
                                        'f8d2eb98e626defe7bcc37762d3af2b7'
                                        .format(self.city))             
            city_json = city_request.json()
            data = {
                'name': city_json['city']['name'],
                'temp': self.to_celsius(city_json['list'][0]['main']['temp']),
                'icon': city_json['list'][0]['weather'][0]['icon'],
                'weather': city_json['list'][0]['weather'][0]['description']
            }
            return data
        except:
            data = "Sorry, unable to get data."
            return data
