import requests
import random
from config.api.api_config import APIConfig
import logging as loger

from config.base_config import BaseConfig
from service import api_commons
from utilities.service.api_base import service_get, service_post, service_delete

pet_id = random.randint(1, 100)
payload = {
    'id': pet_id,
    'category': {
        'id': 1,
        'name': 'TEST',
    },
    'name': 'doggie',
    'photoUrls': [
        'string',
    ],
    'tags': [
        {
            'id': 0,
            'name': 'string',
        },
    ],
    'status': 'available',
}


def create_pet():
    service_post(
        api_url=f"{BaseConfig.BACKEND_URL}{APIConfig.VERSION}{APIConfig.PET}",
        headers=api_commons.create_headers(),
        json_data=payload,
        response_code=requests.codes.ok)
    loger.INFO


def get_pet():
    service_get(
        api_url=f"{BaseConfig.BACKEND_URL}{APIConfig.VERSION}{APIConfig.PET}/{pet_id}",
        header=api_commons.create_headers(),
        response_code=requests.codes.ok)


def delete_pet():
    service_delete(
        api_url=f"{BaseConfig.BACKEND_URL}{APIConfig.VERSION}{APIConfig.PET}/{pet_id}",
        header=api_commons.create_headers(),
        response_code=requests.codes.ok)


def delete_non_existing_pet():
    service_delete(
        api_url=f"{BaseConfig.BACKEND_URL}{APIConfig.VERSION}{APIConfig.PET}/{pet_id}",
        header=api_commons.create_headers(),
        response_code=requests.codes.not_found)
