import logging
import time

from tencentcloud.common.exception import TencentCloudSDKException


class NoopRetryer(object):
    def send_request(self, fn):
        return fn()


class StandardRetryer(object):
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
