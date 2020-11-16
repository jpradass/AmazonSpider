from helper.mail_helper import MailHelper
import spider.spider as spider
import configuration.configuration_handler as configuration_handler

if __name__ == "__main__":
    conf = configuration_handler.Configuration('configuration/products.json')
    products = conf.load_configuration()
    
    update, msg = spider.Spider(products).crawl()
    if update:
        mail_helper = MailHelper()
        mail_helper.send_mail('', msg, "New prices lower")
        mail_helper.close_connection()

        conf.save_configuration(products)
