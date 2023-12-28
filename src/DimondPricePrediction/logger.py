import logging
import os
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"   #logfile path

log_path=os.path.join(os.getcwd(),"logs")                       # log folder path

os.makedirs(log_path,exist_ok=True)                            # dir

LOG_FILEPATH=os.path.join(log_path,LOG_FILE)                    # join folder and file path

#loging config
#formate of log file
logging.basicConfig(level=logging.INFO,
                    filename=LOG_FILEPATH,
                    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s"
                    
)


if __name__ == '__main__':
    logging.info("here again i am tesitng")