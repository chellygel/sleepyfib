from exception import *

class SleepyFib:
    def fib(self, n):
        #Tells us the nth fibonacci number
        self.validate_fib(n)
        if n == 1:
            return 0
        elif n == 2:
            return 1
        else:
            return self.fib(n-1) + self.fib(n-2)

    def validate_fib(self,n):
        #Validates the data before it gets passed into function

        if isinstance(n, int) == False:
            raise NotIntegerError
        elif n < 1:
            raise BadNumberError
        elif n > 30:
            raise AboveMaxNumberError
        else:
            return n
