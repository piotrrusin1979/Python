def deco1(func):
    print("deco1")
    return func

    
def deco2(func):
    print("deco2")
    def miko():
        print("mik")
    return miko
    
@deco2
def g():
    print("g")

g()
g()    
    
exit() 
import time
import functools
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        print("%s took %0.8fs" % (func.__name__, elapsed))
        return result
    return clocked
    
from math import factorial
#@deco1
#@deco2
@clock
def f(x):
    print("factorial(%i) = %i" % (x, factorial(x)))
    
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)
    
"""
Wywraca się dla n=1000
"""    
def silnia(n):
    if n < 2:
        return 1
    return n * silnia(n-1)
    
@clock
def g(x):
    print("silnia(%i) = %i" % (x, silnia(x)))

@clock
def h(x):
    print("fibonacci(%i) = %i" % (x, fibonacci(x)))

    
if __name__ =='__main__':
    f(1000)
    print (f(200) == g(200))
    g(200)
    h(35)
    