# -*- coding: utf-8 -*-
#
# Copyright 1999-2017 Tencent Ltd.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import time
import threading


STATE_CLOSED = 0
STATE_HALF_OPEN = 1
STATE_OPEN = 2


class Counter(object):

    def __init__(self):
        self.failures = 0
        self.total = 0
        self.consecutive_successes = 0
        self.consecutive_failures = 0

    def on_success(self):
        self.total += 1
        self.consecutive_successes += 1
        self.consecutive_failures = 0

    def on_failure(self):
        self.total += 1
        self.failures += 1
        self.consecutive_failures += 1
        self.consecutive_successes = 0

    def clear(self):
        self.failures = 0
        self.total = 0
        self.consecutive_successes = 0
        self.consecutive_failures = 0

    def get_failure_rate(self):
        if self.total == 0:
            return 0.0
        return float(self.failures) / self.total


class CircuitBreaker(object):

    def __init__(self, breaker_setting):
        self.breaker_setting = breaker_setting
        self.lock = threading.Lock()
        self.counter = Counter()
        self.state = STATE_CLOSED
        self.expiry = time.time() + breaker_setting.window_interval
        self.generation = 0

    def ready_to_open(self):
        return (self.counter.failures >= self.breaker_setting.max_fail_num and
                self.counter.get_failure_rate() >= self.breaker_setting.max_fail_percent) or \
               self.counter.consecutive_failures >= 5

    def current_state(self, now):
        if self.state == STATE_CLOSED:
            if self.expiry <= now:
                self.to_new_generation(now)
        elif self.state == STATE_OPEN:
            if self.expiry <= now:
                self.switch_state(STATE_HALF_OPEN, now)
        return self.state, self.generation

    def switch_state(self, new_state, now):
        if self.state == new_state:
            return
        self.state = new_state
        self.to_new_generation(now)

    def to_new_generation(self, now):
        self.generation = (self.generation + 1) % 10
        self.counter.clear()
        if self.state == STATE_CLOSED:
            self.expiry = now + self.breaker_setting.window_interval
        elif self.state == STATE_OPEN:
            self.expiry = now + self.breaker_setting.timeout
        else:  # STATE_HALF_OPEN
            self.expiry = time.time()

    # whether to use the backup region
    def before_requests(self):
        self.lock.acquire()
        now = time.time()
        state, generation = self.current_state(now)
        self.lock.release()
        if state == STATE_OPEN:
            return generation, True
        return generation, False

    def after_requests(self, before, success):
        self.lock.acquire()
        now = time.time()
        state, generation = self.current_state(now)
        self.lock.release()
        # the breaker has entered the next generation, the current results abandon.
        if generation != before:
            return
        if success:
            self.on_success(state, now)
        else:
            self.on_failure(state, now)

    def on_success(self, state, now):
        if state == STATE_CLOSED:
            self.counter.on_success()
        elif state == STATE_HALF_OPEN:
            self.counter.on_success()
            if self.counter.total - self.counter.failures >= self.breaker_setting.max_requests:
                self.switch_state(STATE_CLOSED, now)

    def on_failure(self, state, now):
        if state == STATE_CLOSED:
            self.counter.on_failure()
            if self.ready_to_open():
                self.switch_state(STATE_OPEN, now)
        elif state == STATE_HALF_OPEN:
            self.counter.on_failure()
            self.switch_state(STATE_OPEN, now)
