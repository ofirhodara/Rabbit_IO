import logging
import ecs_logging


logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler('logs/logs.json')
handler.setFormatter(ecs_logging.StdlibFormatter())
logger.addHandler(handler)

if __name__ == '__main__':
    for i in range(0, 5):
        message = f"Write log number {i}"
        print(message)
        logger.debug(message +" - Hi world!")
