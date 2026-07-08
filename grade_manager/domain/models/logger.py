import logging


class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)
        
        handler = logging.StreamHandler()

        formatted = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )
        
        handler.setFormatter(formatted)
        self.logger.addHandler(handler)
        
    def info(self, message):
        self.logger.info(message)
    
    def error(self, message):
        self.logger.error(message)
        
    def warning(self, message):
        self.logger.warning(message)

    def debug(self, message):
        self.logger.debug(message)