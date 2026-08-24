from tencentcloud.common.abstract_client import AbstractClient


def test_empty_response(mocker):
    """测试空响应"""
    resp = mocker.MagicMock()
    resp.iter_lines.return_value = []
    result = list(AbstractClient._process_response_sse(resp))
    assert result == []


def test_single_event(mocker):
    resp = mocker.MagicMock()
    resp.iter_lines.return_value = [
        b'data:some data',
        b'event:myevent',
        b'id:123',
        b'retry:10',
        0
    ]
    expected = [{'data': 'some data', 'event': 'myevent', 'id': '123', 'retry': 10}]
    # 直接迭代生成器而不是转换为列表
    result = []
    for e in AbstractClient._process_response_sse(resp):
        result.append(e)
    assert result == expected


def test_multiple_events(mocker):
    resp = mocker.MagicMock()
    resp.iter_lines.return_value = [
        b'data:data1',
        b'event:event1',
        b'id:1',
        b'',
        b'data:data2',
        b'event:event2',
        b'id:2',
        b'retry:20',
        0
    ]
    expected1 = {'data': 'data1', 'event': 'event1', 'id': '1'}
    expected2 = {'data': 'data2', 'event': 'event2', 'id': '2', 'retry': 20}
    result = list(AbstractClient._process_response_sse(resp))
    assert result == [expected1, expected2]


def test_comment_line(mocker):
    resp = mocker.MagicMock()
    resp.iter_lines.return_value = [
        b':this is a comment',
        b'data:some data',
        b'event:myevent',
        0
    ]
    expected = {'data': 'some data', 'event': 'myevent'}
    result = list(AbstractClient._process_response_sse(resp))
    assert result == [expected]


def test_data_concatenation(mocker):
    resp = mocker.MagicMock()
    resp.iter_lines.return_value = [
        b'data:some data',
        b'data:more data',
        b'event:myevent',
        0
    ]
    expected = {'data': 'some data\nmore data', 'event': 'myevent'}
    result = list(AbstractClient._process_response_sse(resp))
    assert result == [expected]


def test_unexpected_fields(mocker):
    resp = mocker.MagicMock()
    resp.iter_lines.return_value = [
        b'data:some data',
        b'event:myevent',
        b'unknown:some value',
        0
    ]
    expected = {'data': 'some data', 'event': 'myevent'}
    result = list(AbstractClient._process_response_sse(resp))
    assert result == [expected]


def test_retry_conversion(mocker):
    resp = mocker.MagicMock()
    resp.iter_lines.return_value = [
        b'data:some data',
        b'event:myevent',
        b'retry:10',
        0
    ]
    expected = {'data': 'some data', 'event': 'myevent', 'retry': 10}
    result = list(AbstractClient._process_response_sse(resp))
    assert result == [expected]
