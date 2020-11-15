import json
import os

class Configuration:

    def __init__(self, file):
        if not os.path.exists(file):
            print("{} doesn't have products to watch!".format(file))
            os._exit(1)
        self.cfile = open(file)

    def load_configuration(self):
        return json.load(self.cfile)