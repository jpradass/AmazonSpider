from helper.logger_helper import Log
from helper.mail_helper import MailHelper
import spider.spider as spider
import configuration.configuration_handler as configuration_handler

if __name__ == "__main__":
    logger = Log()
    conf = configuration_handler.Configuration('configuration/products.json')
    products = conf.load_configuration()
    logger.info("Configuration loaded")

    update, msg = spider.Spider(products).crawl()
    if update:
        logger.info("Products to report")
        mail_helper = MailHelper()
        mail_helper.send_mail('', msg, "New prices lower")
        
        logger.info("Mail sent")
        mail_helper.close_connection()

        conf.save_configuration(products)
        logger.info("Configuration saved")
    else:
        logger.info("Nothing to report")