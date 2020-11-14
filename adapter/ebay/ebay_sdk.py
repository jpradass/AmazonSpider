from adapter.sdk import SDK
from bs4 import BeautifulSoup

class EbaySDK(SDK):

    def __init__(self, products):
       super().__init__()
       self.products = products

    def get_currentprice(self):
        if self.request is not None:
            soup = BeautifulSoup(self.request.text, 'lxml')
            price = soup.find('span', attrs={"id": "prcIsum"})
            if price is not None: 
                return float(price.text.strip().replace(",", ".")[:-3])
            else:
                return None
        else:
            return None

    def get_products(self):
        return self.products