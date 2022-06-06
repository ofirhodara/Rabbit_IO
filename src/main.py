import logging
from datetime import time
import ecs_logging
from sys import stdout

# Define logger
logger = logging.getLogger('mylogger')
# set logger level
logger.setLevel(logging.DEBUG)

# set stream handler to stdout
consoleHandler = logging.StreamHandler(stdout)
consoleHandler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(consoleHandler)

if __name__ == '__main__':
    for i in range(0, 5):
        message = f"Write log number {i}"
        print(message)
        logger.debug(message +" - Hi world!")

    while True:
        time.sleep(5)
