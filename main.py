import requests

from models.api_response import APIResponse
from dataclass_wizard import fromdict

response = requests.get("https://dummyjson.com/products")

data = response.json()

api_response = 0
