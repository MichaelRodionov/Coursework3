import logging

logger = logging.getLogger("api_loger")
logger.setLevel(logging.INFO)
logger_handler = logging.FileHandler("./log/api_logs.log")
loger_formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
logger_handler.setFormatter(loger_formatter)
logger.addHandler(logger_handler)
