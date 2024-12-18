import logging
from logging import Logger
from typing import Union

from pydantic import BaseModel

app_logger = logging.getLogger("app")


class LogConfig(BaseModel):
    level: str
    format: str


def get_logger(name: str, level: Union[str, int] = "auto") -> logging.Logger:
    r = logging.getLogger(f"{app_logger.name}.{name}")
    if level == "auto":
        level = app_logger.getEffectiveLevel()
    r.setLevel(level)
    return r


def init_loggers(cfg: LogConfig) -> Logger:
    app_logger.setLevel(cfg.level)

    formatter = logging.Formatter(cfg.format)

    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    app_logger.addHandler(console_handler)

    return app_logger
