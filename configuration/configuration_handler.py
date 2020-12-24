import json
import yaml
import os
from typing import Dict

class Configuration:

    def __init__(self, file: str) -> None:
        if not os.path.exists(file):
            print("{} yaml configuration file doesn't exist".format(file))
            os._exit(1)
        self.file = file

    def load_configuration(self) -> Dict:
        return yaml.load(open(self.file, 'r'), Loader=yaml.FullLoader)

    def save_configuration(self, yml: Dict) -> None:
        yaml.dump(yml, open(self.file, 'w+'))