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

# g()
# g()    
    

import time
import functools
def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - t0
        print("%s(%s,%s) took %0.8fs" % (func.__name__, str(args), str(kwargs), elapsed))
        return result
    return clocked
    
from math import factorial
#@deco1
#@deco2
@clock
def f(x):
    print("factorial(%i) = %i" % (x, factorial(x)))

from functools import lru_cache

@lru_cache(maxsize=8)
@clock
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

def fibonacci_gen(end):
    i = 0
    a = 0
    b = 1
    yield a + b
    while i < end :
        i += 1
        a, b = b, a + b
        yield a + b    

@clock
def i(x):
    for y in fibonacci_gen(x):
        ret = y
        # print(y)
    print("fibonacci_gen(%i) = %i" % (x, ret))

'''
From: 
https://pypi.python.org/pypi/memory_profiler

C:\Mikolaj>pip install memory_profiler

decorate suspect function wiht @profile

python -m memory_profiler deco.py

Interesting too:
http://www.rationalgirl.com/blog/html/2013/05/08/profiling_code.html
https://www.datadoghq.com/dg/apm/ts-python-tracing/
'''    
# @profile
def testy():
    # print (f(200) == g(200))
    # f(1000)  # silnia math
    # g(800)   # silnia requr
    print('\n  fibonacci rekurencyjny\n')
    h(50)    # fibonacci requr
    print('\n  fibonacci generator z yield\n')
    i(50)    # fibonacci_gen

    
if __name__ =='__main__':
    testy()