import adapter.amazon.amazon_sdk as asdk

class SDKFactory:

    def __init__(self):
        pass

    def get_sdk(self, brand, products):
        if brand == "amazon":
            return asdk.AmazonSDK(products)
        else:
            return None

