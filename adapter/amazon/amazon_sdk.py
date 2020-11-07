from adapter.sdk import SDK

class AmazonSDK(SDK):

    def __init__(self, products):
       super().__init__()
       self.products = products

    def get_products(self):
        return self.products