import logging
from logging.handlers import TimedRotatingFileHandler
from pathlib import Path

from config import service_config as config, Env


def init_logger(service_name: str, log_level: str) -> logging.Logger:
    logger = logging.getLogger(service_name)
    logger.setLevel(getattr(logging, log_level))
    formatter = logging.Formatter(
        f"%(asctime)s.%(msecs)03dZ [{service_name}] %(levelname)s: %(message)s",
        "%Y-%m-%dT%H:%M:%S",
    )

    console_handler = logging.StreamHandler()
    console_handler.setLevel(getattr(logging, log_level))
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    if config.env != Env.LOCAL:
        log_path = Path(f"/var/log/{service_name}/{service_name}.log")
        rotating_handler = TimedRotatingFileHandler(
            log_path, when="midnight", encoding="utf-8"
        )
        rotating_handler.setLevel(getattr(logging, log_level))
        rotating_handler.setFormatter(formatter)
        logger.addHandler(rotating_handler)

    return logger


logger = init_logger(config.service_name, config.log_level)
