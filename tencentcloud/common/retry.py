import logging
import time

from tencentcloud.common.exception import TencentCloudSDKException


class NoopRetryer(object):
    """configuration without retry

    NoopRetryer is a retry policy that does nothing.
    It is useful when you don't want to retry.
    """

    def send_request(self, fn):
        return fn()


class StandardRetryer(object):
    """Retry configuration

    StandardRetryer is a retry policy that retries on network errors or frequency limitation.
    :param max_attempts: Maximum number of attempts.
    :type max_attempts: int
    :param backoff_fn: A function that takes the number of attempts and returns the number of seconds to sleep before the next retry.
       Default sleep time is 2^n seconds, n is the number of attempts.
    :type backoff_fn: function
    :param logger: A logger to log retry attempts. If not provided, no logging will be performed.
    :type logger: logging.Logger
    """

    def __init__(self, max_attempts=3, backoff_fn=None, logger=None):
        self._max_attempts = max_attempts
        self._backoff_fn = backoff_fn or self.backoff
        self._logger = logger

    def send_request(self, fn):
        resp = None
        err = None

        for n in range(self._max_attempts):
            try:
                resp = fn()
            except TencentCloudSDKException as e:
                err = e

            if not self.should_retry(resp, err):
                if err:
                    raise err
                return resp

            sleep = self._backoff_fn(n)
            self.on_retry(n, sleep, resp, err)
            time.sleep(sleep)

        raise err

    @staticmethod
    def should_retry(resp, err):
        if not err:
            return False

        if not isinstance(err, TencentCloudSDKException):
            return False

        ec = err.get_code()
        if ec in (
                "ClientNetworkError", "ServerNetworkError", "RequestLimitExceeded",
                "RequestLimitExceeded.UinLimitExceeded", "RequestLimitExceeded.GlobalRegionUinLimitExceeded"
        ):
            return True

        return False

    @staticmethod
    def backoff(n):
        return 2 ** n

    def on_retry(self, n, sleep, resp, err):
        if self._logger:
            self._logger.debug("retry: n=%d sleep=%ss err=%s", n, sleep, err)
