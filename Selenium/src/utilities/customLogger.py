import logging
import os

class CustomLogger:
    def __init__(self, log_level):
        self.log_level = log_level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)

        log_file_name = os.path.join(os.path.dirname(__file__), "../../Logs",  "automation.log")
        file_handler = logging.FileHandler(log_file_name)
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
        file_handler.setFormatter(formatter)

        self.logger.addHandler(file_handler)


    def get_logger(self):
        return self.logger
