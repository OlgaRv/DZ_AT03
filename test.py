import pytest
import requests
from main import get_random_cat_image

def test_get_random_cat_image_success(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{
        'url': 'https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg'
    }]

    api_key = 'YOUR_API_KEY'
    image_url = get_random_cat_image(api_key)

    assert image_url == 'https://cdn2.thecatapi.com/images/MTY3ODIyMQ.jpg'

def test_get_random_cat_image_failure(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404

    api_key = 'YOUR_API_KEY'
    image_url = get_random_cat_image(api_key)

    assert image_url is None
