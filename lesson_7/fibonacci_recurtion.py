def fibo_recurtion(n: int, fib_1 = 0, fib_2 = 1) -> int:
    if n <= 1:
        return fib_1 + fib_2
    print(fib_1 + fib_2, end=' ')
    return fibo_recurtion(n - 1, fib_1 + fib_2, fib_1)

n = int(input('input n: '))
print(fibo_recurtion(n))