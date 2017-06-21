def fib_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)
        
        
        
def fib(n):
    for i in range(n):
        yield fib_recursive(i)



for dupcia in fib(20):
    print(dupcia)