#!/usr/bin/env python
from exception import *

class SleepyFib:
    def fib(self, n):
        return list(self.calc_fib(n))

    def calc_fib(self, n):
        a, b = 0, 1
        for _ in xrange(n):
            yield a
            a, b = b, a + b

    def validate_fib(self,n):
        errors = {
        "NotIntegerError" : "Only positive integers, please.",
        "Over9000" : "Your value is over 9000, please try again."
        }

        #Validates the data before it gets passed into function
        if isinstance(n, int) == False:
            response = errors["NotIntegerError"]
        elif n < 1:
            response = errors["NotIntegerError"]
        elif n > 9000:
            response = errors["Over9000"]
        else:
            response = True
        return response