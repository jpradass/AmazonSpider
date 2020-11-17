import logging
from logging import Logger

class Log:

    logger: Logger = None

    def __new__(cls) -> Logger:
        if Log.logger is None:
            Log.logger = logging.getLogger("spider")
            Log.logger.setLevel(logging.INFO)
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)
            ch.setFormatter(logging.Formatter('[%(asctime)s] %(levelname)s - %(message)s'))
            Log.logger.addHandler(ch)
        
        return Log.logger