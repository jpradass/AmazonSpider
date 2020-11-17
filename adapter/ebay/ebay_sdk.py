from adapter.sdk import SDK
from bs4 import BeautifulSoup

class EbaySDK(SDK):

    def __init__(self) -> None:
       super().__init__("Ebay")

    def get_currentprice(self) -> float:
        if self.request is not None:
            soup = BeautifulSoup(self.request.text, 'lxml')
            price = soup.find('span', attrs={"id": "prcIsum"})
            if price is not None: 
                return float(price.text.strip().replace(",", ".")[:-3])
            else:
                return None
        else:
            return None

