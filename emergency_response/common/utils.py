import json

import requests
from django.conf import settings


def map_my_india_api_request(address=None):
    data = settings.MAP_MY_INDIA__PARAMS.copy()
    data['address'] = address

    # location obtain from mapmy india api call
    r = requests.get(url=settings.MAP_MY_INDIA_URL, params=data)
    try:
        if r.status_code == 200:
            # location obtain from mapmy india api call
            data = json.loads(r.json()['data'][0])
            return {'longitude': data['copResults']['longitude'], 'latitude': data['copResults']['latitude']}, True
        else:
            return {}, False
    except Exception:
        return {}, False
