import requests

import config

GET_DOG_BUTTON = "Get Dog!"


def get_dog() -> bytes:
    api_response = requests.get(config.DOG_URL).json()
    image_url = api_response.get("message")
    return requests.get(image_url).content
