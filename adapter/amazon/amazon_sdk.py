from adapter.sdk import SDK
from bs4 import BeautifulSoup

class AmazonSDK(SDK):

    def __init__(self, products):
       super().__init__()
       self.products = products

    def get_currentprice(self):
        if self.request is not None:
            soup = BeautifulSoup(self.request.text, 'lxml')
            # prices = re.search('\d*,\d{0,2}\s€', self.request.text)
            price = soup.find('span', attrs={"id": "price_inside_buybox"})
            if price is not None: 
                return float(price.text.strip().replace(",", ".")[:-1])
            else:
                return None
        else:
            return None

    def get_products(self):
        return self.products