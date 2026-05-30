import logging
import logging.handlers

from tencentcloud.common import abstract_client

LOGGER_NAME = "tencentcloud_sdk_common"


def test_set_stream_logger_default():
    client = abstract_client.AbstractClient(None, None, None)
    client.set_stream_logger()
    assert len(logging.getLogger(LOGGER_NAME).handlers) == 3
