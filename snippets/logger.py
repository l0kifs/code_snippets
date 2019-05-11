import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler()

# The best type of logging for prod from my point of view
# https://docs.python.org/3/howto/logging-cookbook.html#using-file-rotation
# handler = logging.handlers.RotatingFileHandler('log.out', maxBytes=2e+7, backupCount=3)

# Set specific logging level for handler
# handler.setLevel(logging.DEBUG)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(funcName)s - %(lineno)d - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

logger.addHandler(handler)
