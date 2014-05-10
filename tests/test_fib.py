#!/usr/bin/env python
import pytest
from fibonacci import SleepyFib
from exception import *

class TestFib:

    def test_fib_one(self):
        # Verify initial value hasn't changed
        assert SleepyFib().fib(1) == 0

    def test_fib_two(self):
        # Verify set value hasn't changed
        assert SleepyFib().fib(40) == 63245986

    def test_fib_negative_number(self):
        # Verify negative numbers aren't allowed
        with pytest.raises(BadNumberError):
            SleepyFib().fib(-1)

    def test_fib_decimals(self):
        # Verify decimals aren't allowed
        with pytest.raises(NotIntegerError):
            SleepyFib().fib(2.5)

    def test_fib_string(self):
        # Verify strings aren't allowed
        with pytest.raises(NotIntegerError):
            SleepyFib().fib("a string")

    def test_fib_maximum(self):
        # Verify upper boundary is not passed
        with pytest.raises(ExceedMaxNumberError):
            SleepyFib().fib(300001)
