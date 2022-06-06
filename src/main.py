import logging
import time
import ecs_logging
from sys import stdout
import yaml
from src.consts import Config

# Define logger
logger = logging.getLogger('mylogger')

# set logger level
logger.setLevel(logging.DEBUG)

# set stream handler to stdout
consoleHandler = logging.StreamHandler(stdout)
consoleHandler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(consoleHandler)

# config file
with open(Config.PATH) as f:
    config = yaml.load(f, Loader=yaml.FullLoader)


def run():
    # send messages
    # start to read message
    for i in range(0, 5):
        message = f"Write log number {i}"
        logger.debug(message +" - Hi world!")
        time.sleep(3)
    pass


if __name__ == '__main__':
    run()

