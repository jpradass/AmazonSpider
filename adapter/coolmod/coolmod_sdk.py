from adapter.sdk import SDK
from bs4 import BeautifulSoup

class CoolModSDK(SDK):

    def __init__(self) -> None:
        super().__init__("CoolMod")

    def get_currentprice(self) -> float:
        if self.request is not None:
            soup = BeautifulSoup(self.request.text, 'lxml')
            price = soup.find('div', attrs={"class": "container-price-total"})
            if price is not None: 
                return float(price.text.strip().replace(",", ".")[:-1])
            else:
                return None
        else:
            return None
