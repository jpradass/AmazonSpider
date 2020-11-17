from adapter.sdk import SDK
import adapter.amazon.amazon_sdk as asdk
import adapter.ebay.ebay_sdk as esdk

class SDKFactory:

    def __init__(self) -> None:
        pass

    def get_sdk(self, brand: str) -> SDK:
        if brand == "amazon":
            return asdk.AmazonSDK()
        elif brand == "ebay":
            return esdk.EbaySDK()
        else:
            return None

