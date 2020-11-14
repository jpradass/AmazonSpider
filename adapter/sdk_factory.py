import adapter.amazon.amazon_sdk as asdk
import adapter.ebay.ebay_sdk as esdk

class SDKFactory:

    def __init__(self):
        pass

    def get_sdk(self, brand, products):
        if brand == "amazon":
            return asdk.AmazonSDK(products)
        elif brand == "ebay":
            return esdk.EbaySDK(products)
        else:
            return None

