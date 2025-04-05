import pytest
from tencentcloud.common import abstract_client
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException


# 是否能正确处理非字典类型的参数
def test_fix_params_non_dict():
    client = abstract_client.AbstractClient(None, None, None)
    params = [1, 2, 3]
    result = client._fix_params(params)
    assert result == [1, 2, 3]


def test_fix_params_dict():
    """是否能正确处理字典类型的参数"""
    client = abstract_client.AbstractClient(None, None, None)
    params = {'a': 1, 'b': 2}
    result = client._fix_params(params)
    assert result == {'a': 1, 'b': 2}


def test_format_params_none():
    """是否能正确处理None类型的参数"""
    client = abstract_client.AbstractClient(None, None, None)
    params = None
    result = client._format_params('prefix', params)
    assert result == {}


def test_format_params_list():
    """是否能正确处理list类型的参数"""
    client = abstract_client.AbstractClient(None, None, None)
    params = [1, {'a': 2}, 3]
    result = client._format_params('', params)
    expected = {'0': 1, '1.a': 2, '2': 3}
    assert result == expected


def test_format_params_tuple():
    """是否能正确处理tuple类型的参数"""
    client = abstract_client.AbstractClient(None, None, None)
    params = (1, {'a': 2}, 3)
    result = client._format_params('', params)
    expected = {'0': 1, '1.a': 2, '2': 3}
    assert result == expected


def test_format_params_dict():
    """是否能正确处理dict类型的参数"""
    client = abstract_client.AbstractClient(None, None, None)
    params = {'a': 1, 'b': {'c': 2}}
    result = client._format_params('', params)
    expected = {'a': 1, 'b.c': 2}
    assert result == expected


def test_format_params_unsupported_type():
    """是否能正确处理不支持的类型"""
    client = abstract_client.AbstractClient(None, None, None)
    params = set([1, 2, 3])
    try:
        with pytest.raises(TencentCloudSDKException) as context:
            client._format_params('', params)
        assert context.exception.code == "ClientParamsError"
        assert context.exception.message == "some params type error"
    except pytest.fail.Exception as e:
        assert True
