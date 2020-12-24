from helper.influx_helper import Influx
from typing import Dict
from helper.logger_helper import Log
import requests


class GrafanaLogger:

    def __init__(self, grafana_conf: Dict, influx: Influx) -> None:
        self.host = grafana_conf["host"]
        self.port = grafana_conf["port"]
        self.influx = influx
        self.logger = Log()

    def update_product(self, product: Dict) -> None:
        body = "{},store={} value={}".format(product["name"].replace(" ", "_"), product["store"], product["price"])
        res = requests.post("http://{}:{}/write?db={}".format(self.influx.get_host(), str(self.influx.get_port()), self.influx.get_db()), data=body)  

    def healthcheck(self) -> bool:
        return requests.get("http://{}:{}".format(self.host, str(self.port))).status_code == 200