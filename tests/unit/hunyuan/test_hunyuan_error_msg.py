import warnings

from tencentcloud.hunyuan.v20230901.models import ErrorMsg


def test_hunyuan_error_msg():
    msg = ErrorMsg()
    msg.Msg = "Hello World!"
    assert msg.Msg == "Hello World!"

    msg.Code = "InternalError"
    assert msg.Code == "InternalError"


def test_hunyuan_error_msg_deserialize():
    msg = ErrorMsg()
    params = {
        "Msg": "Hello World!",
        "Code": "InternalError",
        "test": "test"
    }
    with warnings.catch_warnings(record=True) as w:
        msg._deserialize(params)
        assert msg.Msg == "Hello World!"
        assert msg.Code == "InternalError"
        assert str(w.pop().message) == "test fileds are useless."
