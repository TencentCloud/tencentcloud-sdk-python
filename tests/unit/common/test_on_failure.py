from tencentcloud.common.circuit_breaker import Counter


def test_on_failure():
    counter = Counter()
    counter.on_failure()
    assert counter.failures == 1
    assert counter.total == 1
    assert counter.consecutive_failures == 1
    assert counter.consecutive_successes == 0


def test_clear():
    counter = Counter()
    counter.clear()
    assert counter.failures == 0
    assert counter.total == 0
    assert counter.consecutive_failures == 0
    assert counter.consecutive_successes == 0


def test_get_failure_rate():
    counter = Counter()
    counter.total = 0
    assert counter.get_failure_rate() == 0.0
    counter.total = 10
    assert counter.get_failure_rate() == 0.0
    counter.failures = 10
    assert counter.get_failure_rate() == 1.0
    counter.failures = 5
    assert counter.get_failure_rate() == 0.5
