import requests
import adapter.amazon.amazon_sdk as asdk

class Spider:
    
    def __init__(self, products):
        self.products = products
        self.asdk = asdk.AmazonSDK()

    def start(self):
        self.asdk.set_url("https://www.amazon.es/Seagate-Barracuda-Disco-Interno-cach%C3%A9/dp/B0713R3Y6F/ref=sr_1_1?__mk_es_ES=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=seagate+barracuda&qid=1604343012&sr=8-1")
        self.asdk.make_request()
        print(self.asdk.get_currentprice()) 