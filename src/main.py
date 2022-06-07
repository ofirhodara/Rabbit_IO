import logging
from sys import stdout
import ecs_logging
import yaml
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from src.rabbit.sender import Sender
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
    sender = Sender('amqp://guest:guest@localhost:5672/%2F?connection_attempts=3&heartbeat=3600')
    sender.run()


if __name__ == '__main__':
    run()
