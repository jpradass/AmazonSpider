from helper.influx_helper import Influx
from helper.grafana_helper import GrafanaLogger
from helper.logger_helper import Log
from typing import Dict, List, Tuple
from adapter.sdk_factory import SDKFactory

class Spider:
    
    def __init__(self, jdata: Dict, conf: Dict) -> None:
        self.jdata = jdata
        self.lsdk = []
        self.sdkf = SDKFactory()
        self.logger = Log()
        self.conf = conf

        for brand in self.jdata["brands"]:
            self.lsdk.append(self.sdkf.get_sdk(brand))

        if (conf["grafana"] and conf["influx"]) is not None:
            self.grafana = GrafanaLogger(conf["grafana"], Influx(conf["influx"]))

    def crawl(self) -> Tuple[List, str]:
        update, msg = list(), ""
        self.logger.info("Starting products crawl...")

        for sdk in self.lsdk:
            for product in self.jdata[sdk.get_jsonname()]:
                sdk.set_url(product["url"])
                sdk.make_request()
                current_price, min, last_check, desired = sdk.get_currentprice(), product["min"], product["last_check"], product["desired"]
                
                if current_price is not None:
                    po = {"name": product["name"], "price": current_price, "url": product["url"]}
                    if min == float(0) or current_price < min:
                        product["min"] = current_price
                        update.append(po) 
                        msg += "{}{} {}{} {}{} {}{}\n".format(sdk.get_name(), "\t| New minimum price! --", product["name"], ":", min, "€ ->", current_price, "€")
                    
                    if current_price < last_check and current_price >= min:
                        update.append(po) 
                        msg += "{}{} {}{} {}{} {}{}\n".format(sdk.get_name(), "\t| Price drop from last check! --", product["name"], ":", last_check, "€ ->", current_price, "€")
                    
                    if current_price < desired:
                        update.append(po) 
                        msg += "{}{} {}{} {}{} {}{}\n".format(sdk.get_name(), "\t| Price under desired! --", product["name"], ":", desired, "€ (desired) ->", current_price, "€")

                    product["last_check"] = current_price

                    if self.grafana is not None:
                        self.grafana.update_product(po)

        return update, msg

    def register_to_grafana(self, product: Dict) -> None:
        self.logger.debug("Sending product to grafana")