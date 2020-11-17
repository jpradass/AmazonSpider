from helper.logger_helper import Log
from typing import Dict, Tuple
from adapter.sdk_factory import SDKFactory

class Spider:
    
    def __init__(self, jdata: Dict) -> None:
        self.jdata = jdata
        self.lsdk = []
        self.sdkf = SDKFactory()
        self.logger = Log()

        for brand in self.jdata["brands"]:
            self.lsdk.append(self.sdkf.get_sdk(brand))

    def crawl(self) -> Tuple[bool, str]:
        update, msg = False, ""
        self.logger.info("Starting products crawl...")

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