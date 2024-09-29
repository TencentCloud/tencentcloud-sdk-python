from tencentcloud.common.circuit_breaker import CircuitBreaker, Counter


class BreakerSetting:
    def __init__(self, window_interval, timeout, max_requests=0, max_fail_num=0, max_fail_percent=0):
        self.window_interval = window_interval
        self.timeout = timeout
        self.max_requests = max_requests
        self.max_fail_num = max_fail_num
        self.max_fail_percent = max_fail_percent


def test_on_success(mocker):
    breaker_setting = BreakerSetting(10, 10)
    cb = CircuitBreaker(breaker_setting)
    mock_counter = mocker.patch.object(cb, 'counter')
    cb.on_success(0, 1)
    mock_counter.on_success.assert_called_once()

    cb1 = CircuitBreaker(breaker_setting)
    mock_switch = mocker.patch.object(cb1, 'switch_state')
    cb1.on_success(1, 1)
    mock_switch.assert_called_once()


def test_on_failure(mocker):
    breaker_setting = BreakerSetting(10, 10)
    cb = CircuitBreaker(breaker_setting)
    mock_switch = mocker.patch.object(cb, 'switch_state')
    cb.on_failure(0, 1)
    mock_switch.assert_called_once()

    cb1 = CircuitBreaker(breaker_setting)
    mock_switch1 = mocker.patch.object(cb1, 'switch_state')
    cb1.on_failure(1, 1)
    mock_switch1.assert_called_once()
