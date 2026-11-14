import warnings

from tencentcloud.hunyuan.v20230901.models import ChatCompletionsRequest


def test_chat_completions_request_init():
    request = ChatCompletionsRequest()
    request.Model = 'gpt-3.5-turbo-0613'
    assert request.Model == 'gpt-3.5-turbo-0613'

    request.Messages = [
        {
            'role': 'user',
            'content': 'Hello, world!'
        }
    ]
    assert request.Messages[0]['role'] == 'user'
    assert request.Messages[0]['content'] == 'Hello, world!'

    request.Stream = True
    assert request.Stream is True

    request.StreamModeration = True
    assert request.StreamModeration is True

    request.TopP = 0.9
    assert request.TopP == 0.9

    request.Temperature = 0.9
    assert request.Temperature == 0.9

    request.EnableEnhancement = True
    assert request.EnableEnhancement is True

    request.Tools = ['gpt-3.5-turbo-0613', '']
    assert request.Tools == ['gpt-3.5-turbo-0613', '']

    request.ToolChoice = 'gpt-3.5-turbo-0613'
    assert request.ToolChoice == 'gpt-3.5-turbo-0613'

    request.CustomTool = ['gpt-3.5-turbo']
    assert request.CustomTool == ['gpt-3.5-turbo']


def test_chat_completions_request_deserialize(mocker):
    request = ChatCompletionsRequest()
    params = {
        "Model": "TestModel",
        "Messages": [{"message_id": 1, "content": "Test message"}],
        "Stream": "TestStream",
        "StreamModeration": "TestStreamModeration",
        "TopP": "TestTopP",
        "Temperature": "TestTemperature",
        "EnableEnhancement": "TestEnableEnhancement",
        "Tools": [1, 2, 3],
        "ToolChoice": "TestToolChoice",
        "CustomTool": "111",
        "test": "test"
    }

    with mocker.patch('tencentcloud.hunyuan.v20230901.models.Message._deserialize', return_value=111) as mock_Message, \
            mocker.patch('tencentcloud.hunyuan.v20230901.models.Tool._deserialize', return_value=222) as mock_Tool, \
            warnings.catch_warnings(record=True) as w:
        request._deserialize(params)
        assert request._Model == 'TestModel'
        assert len(request.Messages) == 1
        assert str(w.pop().message) == "test fileds are useless."
