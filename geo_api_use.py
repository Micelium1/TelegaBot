import cfg
from urllib.request import urlopen
import json


class Coords:
    def __init__(self,longitude,latitude):
        self.longitude = longitude
        self.latitude = latitude




def get_coords(user_input:str) -> Coords:
    geo_response = get_geo_response(
        city_name = user_input
    )
    weather = _parse_geo_response(geo_response)
    return weather


def get_geo_response(city_name:str) -> str:
    url = cfg.geo_api.format(city_name=city_name)
    return urlopen(url).read()


def _parse_longitude(openweather_dict: dict) -> str:
    return openweather_dict[0]["lon"]


def _parse_latitude(openweather_dict: dict) -> str:
    return openweather_dict[0]["lat"]


def _parse_geo_response(geo_response: str) -> Coords:
    openweather_dict = json.loads(geo_response)
    return Coords(
        longitude=float(_parse_longitude(openweather_dict)),latitude=float(_parse_latitude(openweather_dict))
    )
