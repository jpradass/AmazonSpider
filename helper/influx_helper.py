from typing import Dict


class Influx:

    def __init__(this, influx_conf: Dict) -> None:
        this.host = influx_conf["host"]
        this.port = influx_conf["port"]
        this.db = influx_conf["db"]

    def get_host(this) -> str:
        return this.host

    def get_port(this) -> int:
        return this.port

    def get_db(this) -> str:
        return this.db