import sys
import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

def error_message_detail(error):
    _, _, exc_tb = sys.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occurred in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error):
        super().__init__(str(error))
        self.error_message = error_message_detail(error)

    def __str__(self):
        return self.error_message

#if __name__ == "__main__":
#    try:
#        a = 1 / 0
#    except Exception as e:
#        logging.info("Divide by zero")
#        raise CustomException(e)
