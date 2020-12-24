from helper.logger_helper import Log
from helper.mail_helper import MailHelper
import spider.spider as spider
from configuration.configuration_handler import Configuration
from configuration.products_handler import ProductsHandler

if __name__ == "__main__":
    logger = Log()
    conf = Configuration('configuration/configuration.yaml').load_configuration()
    ph = ProductsHandler(conf["products_path"]) 
    logger.info("Configuration loaded")
    products = ph.load_products()
    logger.info("Products loaded from {}".format(conf["products_path"]))

    update, msg = spider.Spider(products, conf).crawl()
    if len(update) > 0:
        logger.info("Products to report")
        mail_helper = MailHelper()
        mail_helper.send_mail('', msg, "New prices lower")
        
        logger.info("Mail sent")
        mail_helper.close_connection()

    else:
        logger.info("Nothing to report")
    
    ph.save_products(products)
    logger.info("Configuration saved")
else:
    print("Exec this file as the main entrypoint! -> python3 init.py")