import requests
from pprint import pprint


class LocationDetails:
    key = 'AIzaSyBSgLU3mfl15Dpra5sYYE_-qPflhWQJjxA'
    geocode_api = 'https://maps.googleapis.com/maps/api/geocode/json'
    distance_api = 'https://maps.googleapis.com/maps/api/directions/json'

    def get_geocode(self, place):
        geo_params = {'address': place, 'key': self.key}
        json = requests.get(self.geocode_api, params=geo_params).json()
        location = json['results'][0]['geometry']['location']
        lat = location['lat']
        lng = location['lng']
        return {'lat': lat, 'lng': lng}

    def get_distance(self, place1, place2):
        loc_params = {'origin': place1, 'destination': place2, 'key': self.key}
        directions = requests.get(self.distance_api, loc_params).json()
        distance = directions['routes'][0]['legs'][0]['distance']['text']
        distance = distance.strip('km')
        distance = distance.strip()
        distance = float(distance)
        return distance

    def get_district(self, place):
        geo_params = {'address': place, 'key': self.key}
        json = requests.get(self.geocode_api, params=geo_params).json()
        district = json['results'][0]['address_components'][1]['long_name']
        return district








