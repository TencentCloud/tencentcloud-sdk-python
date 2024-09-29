from tencentcloud.hunyuan.v20230901.models import QueryHunyuanImageJobResponse


def test_query_hunyuan_image_job_response():
    resp = QueryHunyuanImageJobResponse()
    resp.RequestId = "83k2-2ked02-3sl3"
    assert resp.RequestId == "83k2-2ked02-3sl3"

    resp.JobStatusCode = '0'
    assert resp.JobStatusCode == '0'

    resp.JobStatusMsg = 'success'
    assert resp.JobStatusMsg == 'success'

    resp.JobErrorCode = '704'
    assert resp.JobErrorCode == '704'

    resp.JobErrorMsg = 'job not found'
    assert resp.JobErrorMsg == 'job not found'

    resp.ResultImage = 'http://example.com'
    assert resp.ResultImage == 'http://example.com'

    resp.ResultDetails = {
        '1': 'http://example.com/1',
        '2': 'http://example.com/2',
    }
    assert resp.ResultDetails == {
        '1': 'http://example.com/1',
        '2': 'http://example.com/2', }

    resp.RevisedPrompt = 'hello'
    assert resp.RevisedPrompt == 'hello'


def test_query_hunyuan_image_job_response_deserialize():
    resp = QueryHunyuanImageJobResponse()
    params = {
        'RequestId': '83k2-2ked02-3sl3',
        'JobStatusCode': '0',
        'JobStatusMsg': 'success',
        'JobErrorCode': '704',
        'JobErrorMsg': 'job not found',
        'ResultImage': 'http://example.com',
        'ResultDetails': {
            '1': 'http://example.com/1',
            '2': 'http://example.com/2',
        },
        'RevisedPrompt': 'hello',
    }
    resp._deserialize(params)
    assert resp.RequestId == '83k2-2ked02-3sl3'
    assert resp.JobStatusCode == '0'
    assert resp.JobStatusMsg == 'success'
    assert resp.JobErrorCode == '704'
    assert resp.JobErrorMsg == 'job not found'
    assert resp.ResultImage == 'http://example.com'
