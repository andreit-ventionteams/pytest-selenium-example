import os
import sys
import logging
from rich.logging import RichHandler
from rich.console import Console


class _Logger:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self):
        if self._initialized:
            return
        self._initialized = True

        level_name = os.getenv("LOG_LEVEL", "DEBUG").upper()
        level = getattr(logging, level_name, logging.INFO)

        self._logger = logging.getLogger("framework")
        self._logger.setLevel(level)

        if not self._logger.handlers:
            console = Console(
                stderr=False,
                force_terminal=sys.stdout.isatty(),
                width=int(os.getenv("CONSOLE_WIDTH", "120")),
            )
            handler = RichHandler(
                console=console,
                show_time=True,
                show_level=True,
                show_path=True,
                rich_tracebacks=True,
                tracebacks_show_locals=True,
                markup=True,
                log_time_format="[%Y-%m-%d %H:%M:%S]",
            )
            handler.setLevel(level)
            self._logger.addHandler(handler)

    def get(self) -> logging.Logger:
        return self._logger


def get_logger() -> logging.Logger:
    """Get the singleton logger instance with Rich console output"""
    return _Logger().get()