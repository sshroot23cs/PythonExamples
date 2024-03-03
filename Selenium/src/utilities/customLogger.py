import logging
import queue
from logging.handlers import QueueHandler, QueueListener
import os

class CustomLogger:
    def __init__(self, log_level):
        self.log_level = log_level
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(self.log_level)

        log_file_name = os.path.join(os.path.dirname(__file__), "../../logs", "automation.log")
        file_handler = logging.FileHandler(log_file_name, mode='w')
        formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(threadName)s: %(name)s : %(message)s')
        file_handler.setFormatter(formatter)
        # queue handler to handle logs from multiple threads
        log_queue = queue.Queue(-1)
        queue_handler = QueueHandler(log_queue)
        self.logger.addHandler(queue_handler)
        self.logger.addHandler(file_handler)
        listener = QueueListener(log_queue, file_handler)
        listener.start()
        self.logger.warning('Look out!')
        listener.stop()

    def get_logger(self):
        return self.logger
