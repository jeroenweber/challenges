def fib(n):
    f = 1
    f0 = 1
    f1 = 1
    while (n > 1):
        n = n - 1
        f = f0 + f1
        f0 = f1
        f1 = f
    return f


n = 9
while (n > 0):
    print('fib ' + str(n) + ' = ' + str(fib(n)))
    n = n - 1
