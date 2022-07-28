def fibonacci(n: int) -> int:
    fib_1 = fib_2 = 1
    print(fib_1, fib_2, end=' ')
    for el in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')

fibonacci(10)