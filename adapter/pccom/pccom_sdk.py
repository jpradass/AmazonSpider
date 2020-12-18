from adapter.sdk import SDK
from bs4 import BeautifulSoup

class PcCOMSDK(SDK):

    def __init__(self) -> None:
        super().__init__("PcCom")

    def get_currentprice(self) -> float:
        if self.request is not None:
            soup = BeautifulSoup(self.request.text, 'lxml')
            price = soup.find('div', attrs={"id": "priceBlock"})
            if price is not None: 
                return float(price['data-price'])
            else:
                return None
        else:
            return None

