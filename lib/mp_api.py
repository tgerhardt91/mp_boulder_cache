import requests
import json


def get_routes_for_lat_lon(lat, lon):
    base_url = 'https://www.mountainproject.com/data/get-routes-for-lat-lon?'
    params = {'key': api_key(), 'lat': lat, 'lon': lon, 'minDiff': 'V0',
              'maxDiff': 'V15', 'maxDistance': 50, 'maxResults': 200}

    request = requests.get(base_url, params)

    data = request.json()


def api_key():
    return ''
