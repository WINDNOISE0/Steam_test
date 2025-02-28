import logging
import datetime
import os

import pytest


class Logger:
    separator_template = "-----"
    log_dir = "C:\\Users\\1\\Desktop\\QA\\Auto\\Steam_test\\logs"
    os.makedirs(log_dir, exist_ok=True)

    log_file = os.path.join(log_dir, f"log_{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.log")

    """Я что то сломал во время настройки и теперь конфликты хендлеров и кроме этого ничего не помогает"""
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger(__name__)

    @classmethod
    def add_start_step(cls, method: str, test_name):
        cls.logger.info(cls.separator_template)
        cls.logger.info(f"Test: {test_name}")
        cls.logger.info(f"Start time: {datetime.datetime.now()}")
        cls.logger.info(f"Start method: {method}")
        cls.logger.info(cls.separator_template)

    @classmethod
    def add_end_step(cls):
        """Логирует окончание теста + статус"""
        # outcome = "PASSED" if pytest.session.testsfailed == 0 else "FAILED"
        Logger.info(f"End time: {datetime.datetime.now()}")
        # Logger.info(f"Test result: {outcome}") не работает(
        Logger.info(Logger.separator_template)

    @classmethod
    def error(cls, message: str):
        cls.logger.error(f"ERROR: {message}")

    @classmethod
    def info(cls, message: str):
        cls.logger.info(message)
