from adapter.sdk_factory import SDKFactory

class Spider:
    
    def __init__(self, jdata):
        self.jdata = jdata
        self.lsdk = []
        self.sdkf = SDKFactory()
        
        for brand in self.jdata["brands"]:
            self.lsdk.append(self.sdkf.get_sdk(brand))

    def crawl(self):
        update, msg = False, ""
        for sdk in self.lsdk:
            for product in self.jdata[sdk.get_jsonname()]:
                sdk.set_url(product["url"])
                sdk.make_request()
                current_price, min = sdk.get_currentprice(), product["min"]
                
                if min == float(0) or current_price < min:
                    product["min"] = current_price
                    update = True
                    msg += "{}{} {}{} {}{} {}{}\n".format(sdk.get_name(), "\t|", product["name"], ":", min, "€ ->", current_price, "€")
        
        return update, msg