import warnings
import pytest

import logging
from tencentcloud.common import abstract_client


def test_empty_handler_emit():
    warnings.simplefilter('error')
    empty_handler = abstract_client.EmptyHandler()

    log_record = logging.LogRecord("test_logger", logging.INFO, "", 0, "Test message", (), None)
    empty_handler.emit(log_record)
    assert True
