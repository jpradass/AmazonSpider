import json
import os
from typing import Dict

class ProductsHandler:

    def __init__(self, file: str) -> None:
        if not os.path.exists(file):
            print("{} doesn't have products to watch!".format(file))
            os._exit(1)
        self.file = file

    def load_products(self) -> Dict:
        return json.load(open(self.file, 'r'))

    def save_products(self, jobj: Dict) -> None:
        json.dump(jobj, open(self.file, 'w+'))