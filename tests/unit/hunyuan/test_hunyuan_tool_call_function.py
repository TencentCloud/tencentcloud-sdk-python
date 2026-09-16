import warnings

from tencentcloud.hunyuan.v20230901.models import ToolCallFunction


def test_hunyuan_tool_call_function():
    function = ToolCallFunction()
    function.Name = "function"
    assert function.Name == "function"

    function.Arguments = ["arg1", "arg2"]
    assert function.Arguments == ["arg1", "arg2"]


def test_hunyuan_tool_call_function_deserialize():
    function = ToolCallFunction()
    params = {
        "Name": "function",
        "Arguments": ["arg1", "arg2"],
        "test": "test"
    }
    with warnings.catch_warnings(record=True) as w:
        function._deserialize(params)
        assert function.Name == "function"
        assert str(w.pop().message) == "test fileds are useless."
