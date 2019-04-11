import requests
from .payloads import get_problem_payload
from gettingstarted import settings
import sys


MaxDistance = 50
MaxResults = 500
BaseUrl = 'https://www.mountainproject.com/data/get-routes-for-lat-lon?'


def get_boulders_at_coordinates(lat, lon):
    params = build_params(api_key(), lat, lon)
    request = requests.get(BaseUrl, params)

    log_call(BaseUrl + params)

    data = request.json()
    return get_problem_payload(data)


def get_routes_at_coordinates(lat, lon):
    params = build_params(api_key(), lat, lon, for_boulders=False)
    request = requests.get(BaseUrl, params)

    log_call(BaseUrl+params)

    data = request.json()
    return get_problem_payload(data)


def api_key():
    return settings.MP_API_KEY


def build_params(key, lat, lon, for_boulders=True):
    min_diff = 'V0' if for_boulders else '5.6'
    max_diff = 'V15' if for_boulders else '5.15'

    return {'key': key, 'lat': lat, 'lon': lon, 'minDiff': min_diff,
            'maxDiff': max_diff, 'maxDistance': MaxDistance, 'maxResults': MaxResults}


def log_call(url):
    sys.stdout('requesting data from: ' + url)


