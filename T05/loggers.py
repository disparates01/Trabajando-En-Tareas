
from logging import getLogger, DEBUG, StreamHandler, Formatter

def logger(texto):
    logger = getLogger(__name__)
    logger.setLevel(DEBUG)
    formatter = Formatter(
        '%(levelname)s[%(name)s, linea %(lineno)d]:   %(message)s ')
    stream_handler = StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
    logger.debug(texto)