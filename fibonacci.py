#!/usr/bin/env python
from exception import *

class SleepyFib:
    def fib(self, n):
        # Verify valid number before submitting
        self.validate_fib(n)
        # Execute fib calculation
        return self.calc_fib(n)

    def calc_fib(self, n):
        # Tells us the nth fibonacci number
        a,b = 0,1
        if n == 1:
            return a
        elif n == 2:
            return b
        else:
            for x in range(1,n):
                a, b = b, a+b
            return a


    def validate_fib(self,n):
        #Validates the data before it gets passed into function

        if isinstance(n, int) == False:
            raise NotIntegerError
        elif n < 1:
            raise BadNumberError
        elif n > 300000:
            raise ExceedMaxNumberError
        else:
            pass