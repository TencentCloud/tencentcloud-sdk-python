from tencentcloud.common.http.request import ResponsePrettyFormatter


class HttpResponse:
    def __init__(self, raw, status_code, reason, headers, text):
        self.raw = raw
        self.status_code = status_code
        self.reason = reason
        self.headers = headers
        self.text = text


class Raw:
    def __init__(self, version):
        self.version = version


def test_response_pretty_formatter():
    raw = Raw("2020-01-01T00:00:")
    resp = HttpResponse(raw, status_code=200, reason="OK", headers={"Content-Type": "application/json"},
                        text="{\"name\": \"zhangsan\"}")
    formatter = ResponsePrettyFormatter(resp)
    assert formatter._format_body is True
    result = formatter.__str__()
    assert '{"name": "zhangsan"}' in result
    assert "2020-01-01T00:00:" in result
    assert "Content-Type" in result
    assert "OK" in result
    assert "200" in result


def test_response_pretty_formatter_str_ver():
    assert ResponsePrettyFormatter.str_ver(10) == "HTTP/1.0"
    assert ResponsePrettyFormatter.str_ver(11) == "HTTP/1.1"
    assert ResponsePrettyFormatter.str_ver(20) == "HTTP/2.0"
    assert ResponsePrettyFormatter.str_ver(99) == "99"
