import adapter.amazon.amazon_sdk as asdk

class Spider:
    
    def __init__(self, jsonf):
        self.jsonf = jsonf
        self.lsdk = []
        
        for brand in self.jsonf["brands"]:
            self.lsdk.append(asdk.AmazonSDK(self.jsonf[brand]))

    def start(self):
        for sdk in self.lsdk:
            for product in sdk.get_products():
                sdk.set_url(product["url"])
                sdk.make_request()
                current_price, min = sdk.get_currentprice(), product["min"]
                print(product["name"], ":", current_price)

                if min == 0 or current_price < min:
                    product["min"] = current_price   