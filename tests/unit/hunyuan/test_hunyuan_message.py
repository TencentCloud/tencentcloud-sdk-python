import warnings

from tencentcloud.hunyuan.v20230901.models import Message


def test_hunyuan_message():
    msg = Message()
    msg.Role = "admin"
    assert msg.Role == "admin"

    msg.Content = "hello"
    assert msg.Content == "hello"

    msg.Contents = ["hello", "world"]
    assert msg.Contents == ["hello", "world"]

    msg.ToolCallId = "123456"
    assert msg.ToolCallId == "123456"

    msg.ToolCalls = ["123456", "789012"]
    assert msg.ToolCalls == ["123456", "789012"]


def test_hunyuan_message_deserialize(mocker):
    msg = Message()
    params = {
        "Role": "admin",
        "Content": ["hello"],
        "Contents": ["hello", "world"],
        "ToolCallId": "123456",
        "ToolCalls": ["123456", "789012"],
        "test": "test",
    }
    with mocker.patch('tencentcloud.hunyuan.v20230901.models.Content._deserialize', return_value=111), \
            mocker.patch('tencentcloud.hunyuan.v20230901.models.ToolCall._deserialize', return_value=222), \
            warnings.catch_warnings(record=True) as w:
        msg._deserialize(params)
        assert msg.Role == "admin"
        assert str(w.pop().message) == "test fileds are useless."
