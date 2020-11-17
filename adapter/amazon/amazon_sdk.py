from adapter.sdk import SDK
from bs4 import BeautifulSoup

class AmazonSDK(SDK):

    def __init__(self) -> None:
       super().__init__("Amazon")

    def get_currentprice(self) -> float:
        if self.request is not None:
            soup = BeautifulSoup(self.request.text, 'lxml')
            # prices = re.search('\d*,\d{0,2}\s€', self.request.text)
            price = soup.find('span', attrs={"id": "price_inside_buybox"})
            if price is None: 
                price = soup.find('span', attrs={"id": "newBuyBoxPrice"})
            
            return float(price.text.strip().replace(",", ".")[:-1])
        else:
            return None
