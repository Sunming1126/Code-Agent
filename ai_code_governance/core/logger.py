import logging
import os

def get_logger(path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    logger = logging.getLogger("governance")
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        fh = logging.FileHandler(path)
        formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        fh.setFormatter(formatter)
        logger.addHandler(fh)

    return logger