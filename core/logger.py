import os
import sys
from loguru import logger


# -------------------------------
# Config
# -------------------------------
LOG_DIR = os.getenv("LOG_DIR", "reports/logs")
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

os.makedirs(LOG_DIR, exist_ok=True)


# -------------------------------
# Logger Setup
# -------------------------------
def setup_logger():
    # Remove default logger
    logger.remove()

    # Console Logger
    logger.add(
        sys.stdout,
        level=LOG_LEVEL,
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
               "<level>{level}</level> | "
               "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> | "
               "<level>{message}</level>",
        colorize=True
    )

    # File Logger (rotating)
    logger.add(
        f"{LOG_DIR}/automation.log",
        level=LOG_LEVEL,
        format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {process} | {thread} | "
               "{name}:{function}:{line} | {message}",
        rotation="10 MB",
        retention="7 days",
        compression="zip"
    )

    # Error File (separate)
    logger.add(
        f"{LOG_DIR}/errors.log",
        level="ERROR",
        format="{time} | {level} | {message}",
        rotation="5 MB",
        retention="10 days"
    )

    return logger


# Initialize once
log = setup_logger()