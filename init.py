import spider.spider as spider
import configuration.configuration_handler as configuration_handler

if __name__ == "__main__":
    conf = configuration_handler.Configuration('configuration/products.json')
    products = conf.load_configuration()
    
    spider.Spider(products).crawl()
