#DEBUG
#INFO
#WARNING
#ERROR
#CRITICAL
import logging
logging.basicConfig(level=logging.INFO)
logging.info("Info")
logging.error("Error")
logging.debug("Debug")
logging.critical("Crirtical")
logging.warning("Warning")
logging.log(logging.CRITICAL, "Critical using log method")
logger=logging.getLogger("MyLogger")
handler = logging.FileHandler("mylog.log")
handler.setLevel(logging.INFO)
logger.addHandler(handler)
logger.log(logging.INFO,"Hello")
logger.log(logging.WARNING,"Warning")