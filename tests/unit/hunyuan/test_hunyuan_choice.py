import warnings
import unittest
from tencentcloud.hunyuan.v20230901.models import Choice


def test_hunyuan_choice():
    choice = Choice()

    choice.FinishReason = "test"
    assert choice.FinishReason == "test"

    choice.Delta = "test"
    assert choice.Delta == "test"

    choice.Message = "test"
    assert choice.Message == "test"


def test_hunyuan_choice_deserialize(mocker):
    choice = Choice()
    params = {"Delta": "111", "Message": "222", "FinishReason": "333", "fake": "444"}
    with mocker.patch('tencentcloud.hunyuan.v20230901.models.Message._deserialize', return_value=111) as mock_Message, \
            mocker.patch('tencentcloud.hunyuan.v20230901.models.Delta._deserialize', return_value=222) as mock_Delta, \
            warnings.catch_warnings(record=True) as captured_warnings:
        choice._deserialize(params)
        assert choice._FinishReason == "333"
        assert len(captured_warnings) == 1
        assert 'fake fileds are useless.' in str(captured_warnings[0].message)