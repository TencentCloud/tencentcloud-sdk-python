from tencentcloud.common.http.pre_conn import PreConnAdapter, PreConnPoolManager


def test_pre_conn_adapter():
    adapter = PreConnAdapter(conn_pool_size=10)
    assert adapter._conn_pool_size == 10
    adapter.init_poolmanager()
    assert isinstance(adapter.poolmanager, PreConnPoolManager)
