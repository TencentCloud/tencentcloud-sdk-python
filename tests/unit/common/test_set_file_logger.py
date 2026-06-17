import logging
import logging.handlers

from tencentcloud.common import abstract_client
from tencentcloud.common.abstract_client import logger

LOGGER_NAME = "tencentcloud_sdk_common"


def test_set_file_logger_default():
    client = abstract_client.AbstractClient(None, None, None)
    client.set_file_logger('test.log')
    assert len(logging.getLogger(LOGGER_NAME).handlers) == 2
    assert hasattr(logger, 'handlers') is True
    assert logger.level == logging.DEBUG
