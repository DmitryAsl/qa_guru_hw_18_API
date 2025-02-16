from dataclasses import dataclass


@dataclass
class Product:
    name: str
    id: int
    count: int


product_1 = Product(name="Health Book", id=22, count=2)
product_2 = Product(name="Fiction", id=45, count=1)
