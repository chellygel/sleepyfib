#!/usr/bin/env python
class SleepyFib:
    errors = {
        "NotIntegerError" : "Only positive integers, please",
        "Over9000Error" : "Your value is over 9000, please try again"
        }

    def fib(self, n):
        return list(self.calc_fib(n))

    def calc_fib(self, n):
        a, b = 0, 1
        for _ in xrange(n):
            yield a
            a, b = b, a + b

    def validate_fib(self,n):
        #Validates the data before it gets passed into function
        if isinstance(n, int) == False:
            response = self.errors["NotIntegerError"]
        elif n < 1:
            response = self.errors["NotIntegerError"]
        elif n > 9000:
            response = self.errors["Over9000Error"]
        else:
            response = True
        return response