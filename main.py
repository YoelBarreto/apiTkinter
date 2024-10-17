import requests

from models.APIResponse import APIResponse
from dataclass_wizard import fromdict

response = requests.get("https://dummyjson.com/products")
data_dict = response.json()
product_list = fromdict(APIResponse, data_dict)

for product in product_list.products:
    print(product.title)

data = response.json()
api_response = 0

