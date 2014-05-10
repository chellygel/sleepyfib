#!/usr/bin/env python
from exception import *

class SleepyFib:
    def fib(self, n):
        # Verify valid number before submitting
        self.validate_fib(n)
        # Execute fib calculation
        return list(self.calc_fib(n))

    def calc_fib(self, n):
        a, b = 0, 1
        for _ in xrange(n):
            yield a
            a, b = b, a + b

    def validate_fib(self,n):
        #Validates the data before it gets passed into function

        if isinstance(n, int) == False:
            raise NotIntegerError
        elif n < 1:
            raise BadNumberError
        elif n > 8000:
            raise ExceedMaxNumberError
        else:
            pass