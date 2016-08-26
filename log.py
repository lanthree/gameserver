import logging

logging.basicConfig(filename="example.log", \
	level=logging.DEBUG, \
	format="[%(asctime)s] [%(levelname)s] [@ %(filename)s line:%(lineno)d] [channel:%(name)s] %(message)s")

#logging.error("error")
#logging.warning("warning")
#logging.debug("debug")
#logging.info("info")

logger = logging.getLogger("TEST")
logger.debug("This is debug message")
