from abc import ABC, abstractmethod
import requests

class SDK(ABC):

    def __init__(self):
        self.url = None
        self.request = None
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.27 Safari/537.36 Edg/87.0.664.18'}

    def set_url(self, url):
        self.url = url

    def make_request(self):
        self.request = requests.get(self.url, headers=self.headers)
        while self.request.status_code != 200:
            self.request = requests.get(self.url, headers=self.headers)

    @abstractmethod
    def get_currentprice(self):
        pass

    @abstractmethod
    def get_products(self):
        pass