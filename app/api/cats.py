import requests

import config

GET_CAT_BUTTON = "Get Cat!"


def get_cat() -> bytes:
    return requests.get(config.CAT_URL).content
