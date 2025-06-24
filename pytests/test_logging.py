import logging


def test_logname():
    logger = logging.getLogger(__name__)


    fileHandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    fileHandler.setFormatter(formatter)

    logger.addHandler(fileHandler) #filehandler object

    logger.setLevel(logging.INFO)
    logger.debug("A debug statement is printed")
    logger.info("A info statement is printed")
    logger.warning("A warning statement is printing")
    logger.error("A error statement is printing")
    logger.critical("A critical statement is printing")
