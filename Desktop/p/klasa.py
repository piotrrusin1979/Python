def fib_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_r(n-1) + fib_r(n-2)
        
        
        
def fib(n):
    for i in range(n):
        yield fib_r(i)



for dupcia in fib(20):
    print(dupcia)

