from dataclasses import dataclass
from models.dimensions import Dimensions
from models.review import Review
from models.meta import Meta
from typing import List

@dataclass
class Product:
    id : int
    title: str
    description: str
    category: str
    price: float
    discountPercentage: float
    rating: float
    stock: int
    tags: List[str]
    sku: str
    dimensions: Dimensions
    warrantyInformation: str
    shippingInformation: str
    availabilityStatus: str
    reviews: List[Review]
    returnPolicy: str
    minimumOrderQuantity: int
    meta: Meta
    images: List[str]
    thumbnail: str
    brand: str = None