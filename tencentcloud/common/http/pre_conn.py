#!/usr/bin/python
# -*- coding: utf-8 -*-
import logging
import threading

from requests.adapters import HTTPAdapter
from urllib3 import HTTPSConnectionPool, PoolManager, HTTPConnectionPool

logger = logging.getLogger("tencentcloud_sdk_common")


class HTTPSPreConnPool(HTTPSConnectionPool):
    _close_signal = {}

    def __init__(self, *args, **kwargs):
        super(HTTPSPreConnPool, self).__init__(*args, **kwargs)
        # clear the pool
        for _ in range(self.pool.maxsize):
            self.pool.get()
        self._conn_producer = threading.Thread(target=self._conn_producer_loop)
        self._conn_producer.setDaemon(True)
        self._conn_producer.start()

    def _conn_producer_loop(self):
        while True:
            conn = super(HTTPSPreConnPool, self)._new_conn()
            conn.connect()
            logger.debug("HTTPSPreConnPool: created a new conn")
            self.pool.put(conn)


class HTTPPreConnPool(HTTPConnectionPool):
    _close_signal = {}

    def __init__(self, *args, **kwargs):
        super(HTTPPreConnPool, self).__init__(*args, **kwargs)
        # clear the pool
        for _ in range(self.pool.maxsize):
            self.pool.get()
        self._conn_producer = threading.Thread(target=self._conn_producer_loop)
        self._conn_producer.setDaemon(True)
        self._conn_producer.start()

    def _conn_producer_loop(self):
        while True:
            conn = super(HTTPPreConnPool, self)._new_conn()
            conn.connect()
            logger.debug("HTTPSPreConnPool: created a new conn")
            self.pool.put(conn)


class PreConnPoolManager(PoolManager):
    def __init__(self, pool_size, *args, **kwargs):
        self._pool_size = pool_size
        super(PreConnPoolManager, self).__init__(*args, **kwargs)

    def _new_pool(self, scheme, host, port, request_context):
        if scheme == 'https':
            return HTTPSPreConnPool(host, port, maxsize=self._pool_size - 1)
        if scheme == 'http':
            return HTTPPreConnPool(host, port, maxsize=self._pool_size - 1)
        return super(PreConnPoolManager, self)._new_pool(scheme, host, port, request_context)


class PreConnAdapter(HTTPAdapter):
    def __init__(self, conn_pool_size, *args, **kwargs):
        self._conn_pool_size = conn_pool_size
        super(PreConnAdapter, self).__init__(*args, **kwargs)

    def init_poolmanager(self, *args, **kwargs):
        self.poolmanager = PreConnPoolManager(self._conn_pool_size, *args, **kwargs)
