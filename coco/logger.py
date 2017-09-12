#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

import os
import logging
from logging import StreamHandler
from logging.handlers import TimedRotatingFileHandler

from .conf import config
from . import PROJECT_DIR

LOG_LEVELS = {
    'DEBUG': logging.DEBUG,
    'INFO': logging.INFO,
    'WARN': logging.WARNING,
    'WARNING': logging.WARNING,
    'ERROR': logging.ERROR,
    'FATAL': logging.FATAL,
    'CRITICAL': logging.CRITICAL,
}


def create_logger():
    level = config.get('LOG_LEVEL', None)
    level = LOG_LEVELS.get(level, logging.INFO)
    log_dir = config.get('LOG_DIR', os.path.join(PROJECT_DIR, 'logs'))
    log_path = os.path.join(log_dir, 'coco.log')
    logger = logging.getLogger('coco')

    main_formatter = logging.Formatter(
        fmt='%(asctime)s [%(module)s %(levelname)s] %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S')
    console_handler = StreamHandler()
    file_handler = TimedRotatingFileHandler(
        filename=log_path, when='D', backupCount=10)

    for handler in [console_handler, file_handler]:
        handler.setFormatter(main_formatter)
        logger.addHandler(handler)

    logger.setLevel(level)


def get_logger(name):
    logger = logging.getLogger('coco')
    return logger

create_logger()
