import warnings

from tencentcloud.hunyuan.v20230901.models import Tool


def test_hunyuan_tool():
    tool = Tool()
    tool.Type = 'form-data'
    assert tool.Type == 'form-data'

    tool.Function = 'mock_function'
    assert tool.Function == 'mock_function'


def test_hunyuan_tool_deserialize(mocker):
    tool = Tool()
    params = {
        'Type': 'form-data',
        'Function': 'mock_function',
        'test': 'test'
    }
    with mocker.patch('tencentcloud.hunyuan.v20230901.models.ToolFunction._deserialize', return_value=111), \
            warnings.catch_warnings(record=True) as w:
        tool._deserialize(params)
        assert tool.Type == 'form-data'
        assert str(w.pop().message) == "test fileds are useless."
