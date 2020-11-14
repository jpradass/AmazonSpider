from adapter.sdk_factory import SDKFactory

class Spider:
    
    def __init__(self, jsonf):
        self.jsonf = jsonf
        self.lsdk = []
        self.sdkf = SDKFactory()
        
        for brand in self.jsonf["brands"]:
            self.lsdk.append(self.sdkf.get_sdk(brand, self.jsonf[brand]))

    def crawl(self):
        for sdk in self.lsdk:
            for product in sdk.get_products():
                sdk.set_url(product["url"])
                sdk.make_request()
                current_price, min = sdk.get_currentprice(), product["min"]
                print(sdk.get_name(), "\t|", product["name"], ":", current_price, "€")

                if min == float(0) or current_price < min:
                    product["min"] = current_price   