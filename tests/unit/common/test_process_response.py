from tencentcloud.common import abstract_client


class Response:
    def __init__(self, headers, body):
        self.headers = headers
        self.body = body


def test_process_response_sse(mocker):
    client = abstract_client.AbstractClient(None, None)
    resp = Response({'Content-Type': 'text/event-stream'}, None)
    resp_type = 'json'
    _process_response_sse = mocker.patch.object(client, '_process_response_sse')
    client._process_response(resp, resp_type)
    client._process_response_sse.assert_called_once()


def test_process_response_json(mocker):
    client = abstract_client.AbstractClient(None, None)
    resp = Response({'Content-Type': 'json/event-stream'}, None)
    resp_type = 'json'
    _process_response_sse = mocker.patch.object(client, '_process_response_json')
    client._process_response(resp, resp_type)
    client._process_response_json.assert_called_once()