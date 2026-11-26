from tencentcloud.common.http.pre_conn import PreConnPoolManager, HTTPSPreConnPool, HTTPPreConnPool


def test_https_pre_conn_pool(mocker):
    pool_manager = PreConnPoolManager(pool_size=10)
    assert pool_manager._pool_size == 10
    pool = pool_manager._new_pool('https', 'example.com', 80, None)
    assert isinstance(pool, HTTPSPreConnPool)

    pool = pool_manager._new_pool('http', 'example.com', 80, None)
    assert isinstance(pool, HTTPPreConnPool)
