import asyncio
import logging

from tencentcloud.common.exception import TencentCloudSDKException
from tencentcloud.common.retry import NoopRetryer as SyncNoopRetryer, StandardRetryer as SyncStandardRetryer


class NoopRetryer(SyncNoopRetryer):
    """configuration without retry

    NoopRetryer is a retry policy that does nothing.
    It is useful when you don't want to retry.
    """

    async def send_request_async(self, fn):
        return await fn()


class StandardRetryer(SyncStandardRetryer):
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

    async def send_request_async(self, fn):
        resp = None
        err = None

        for n in range(self._max_attempts):
            try:
                resp = await fn()
            except TencentCloudSDKException as e:
                err = e

            if not self.should_retry(resp, err):
                if err:
                    raise err
                return resp

            sleep = self._backoff_fn(n)
            await self.on_retry(n, sleep, resp, err)
            await asyncio.sleep(sleep)

        raise err

    async def on_retry(self, n, sleep, resp, err):
        if self._logger:
            self._logger.debug("retry: n=%d sleep=%ss err=%s", n, sleep, err)
