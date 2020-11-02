import json
import os
import spider.spider as spider

if __name__ == "__main__":
    if not os.path.exists('products.json'):
        print("products.json doesn't have products to watch")
        os._exit(1)

    file = open('products.json')
    products = json.load(file)
    spider.Spider(products).start()
