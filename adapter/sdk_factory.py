from adapter.sdk import SDK
import adapter.amazon.amazon_sdk as asdk
import adapter.ebay.ebay_sdk as esdk
import adapter.pccom.pccom_sdk as pcsdk
import adapter.coolmod.coolmod_sdk as cmsdk

class SDKFactory:

    def __init__(self) -> None:
        pass

    def get_sdk(self, brand: str) -> SDK:
        if brand == "amazon":
            return asdk.AmazonSDK()
        elif brand == "ebay":
            return esdk.EbaySDK()
        elif brand == "pccom":
            return pcsdk.PcCOMSDK()
        elif brand == "coolmod":
            return cmsdk.CoolModSDK()
        else:
            return None

