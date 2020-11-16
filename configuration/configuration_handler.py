import json
import os

class Configuration:

    def __init__(self, file):
        if not os.path.exists(file):
            print("{} doesn't have products to watch!".format(file))
            os._exit(1)
        self.file = file

    def load_configuration(self):
        return json.load(open(self.file, 'r'))

    def save_configuration(self, jobj):
        json.dump(jobj, open(self.file, 'w+'))