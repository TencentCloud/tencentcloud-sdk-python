import requests
from mock.mock import patch

from tencentcloud.common.http.request import ProxyConnection


class TestProxyConnection:
    def test_default_proxy(self):
        conn = ProxyConnection(host="example.com")
        assert conn.request_host == "example.com"
        assert conn.timeout == 60
        assert conn.proxy is None
        assert conn.certification is not None
        assert conn.request_length == 0
        assert isinstance(conn._session, requests.Session)

    @patch('tencentcloud.common.http.request._get_proxy_from_env')
    def test_with_proxy(self, mock_proxy_from_env):
        # 存在proxy时
        conn = ProxyConnection(host="example.com", proxy="http://127.0.0.1:8080")
        assert conn.request_host == "example.com"
        assert conn.proxy == {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}
        # 不存在proxy时
        mock_proxy_from_env.return_value = "http://127.0.0.1:8080"
        conn = ProxyConnection(host="example.com")
        assert conn.request_host == "example.com"
        assert conn.proxy == {"http": "http://127.0.0.1:8080", "https": "http://127.0.0.1:8080"}