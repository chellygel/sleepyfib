#!/usr/bin/env python
import pytest
import requests
from fibonacci import SleepyFib


class TestFib:
    """
    Tests performed against fibonnacci code
    """

    def test_fib_one(self):
        # Verify initial value hasn't changed
        result = SleepyFib().fib(1)
        assert result[-1] == 0

    def test_fib_two(self):
        # Verify set value hasn't changed
        result = SleepyFib().fib(40)
        assert result[-1] == 63245986


class TestAPI:
    """
    Tests performed against SleepyFib API.

    Uses requests directly and compares json to expected outcomes.
    """

    def test_fib_negative(self):
        # Verify negative numbers aren't allowed
        result = requests.get("http://localhost:5000/sleepyfib/api/fib/-5")
        message = SleepyFib().errors["NotIntegerError"]
        expected_response = {"Error!": message}
        assert result.json() == expected_response

    def test_fib_decimals(self):
        # Verify decimals aren't allowed
        result = requests.get("http://localhost:5000/sleepyfib/api/fib/2.5")
        message = SleepyFib().errors["NotIntegerError"]
        expected_response = {"Error!": message}
        assert result.json() == expected_response

    def test_fib_string(self):
        # Verify strings aren't allowed
        result = requests.get("http://localhost:5000/sleepyfib/api/fib/string")
        message = SleepyFib().errors["NotIntegerError"]
        expected_response = {"Error!": message}
        assert result.json() == expected_response

    def test_fib_maximum(self):
        # Verify upper boundary is not passed
        result = requests.get("http://localhost:5000/sleepyfib/api/fib/9001")
        message = SleepyFib().errors["Over9000Error"]
        expected_response = {"Error!": message}
        assert result.json() == expected_response