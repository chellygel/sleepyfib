#!/usr/bin/env python
class SleepyFib:
    """
    Contains the calculation and validation for app
    """
    errors = {
        "NotIntegerError": "Only positive integers, please",
        "Over9000Error": "Your value is over 9000, please try again"
        }

    def fib(self, n):
        # Returns a list from the result of calc_fib generator

        return list(self.calc_fib(n))

    def calc_fib(self, n):
        # Fibonacci sequence generator
        a, b = 0, 1
        for _ in xrange(n):
            yield a
            a, b = b, a + b

    def validate_fib(self, n):
        # Validates data before calc_fib generator is called.
        if isinstance(n, int) is False:
            response = self.errors["NotIntegerError"]
        elif n < 1:
            response = self.errors["NotIntegerError"]
        elif n > 9000:
            response = self.errors["Over9000Error"]
        else:
            response = True
        return response