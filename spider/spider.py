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
                current_price, min, last_check, desired = sdk.get_currentprice(), product["min"], product["last_check"], product["desired"]
                
                if current_price is not None:
                    if min == float(0) or current_price < min:
                        product["min"] = current_price
                        update = True
                        msg += "{}{} {}{} {}{} {}{}\n".format(sdk.get_name(), "\t| New minimum price! --", product["name"], ":", min, "€ ->", current_price, "€")
                    
                    if current_price < last_check and current_price >= min:
                        update = True
                        msg += "{}{} {}{} {}{} {}{}\n".format(sdk.get_name(), "\t| Price drop from last check! --", product["name"], ":", last_check, "€ ->", current_price, "€")
                    
                    if current_price < desired:
                        update = True
                        msg += "{}{} {}{} {}{} {}{}\n".format(sdk.get_name(), "\t| Price under desired! --", product["name"], ":", desired, "€ (desired) ->", current_price, "€")

                    product["last_check"] = current_price

        return update, msg