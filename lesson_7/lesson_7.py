def fibo_recurtion(n: int) -> int:
    if n <= 1:
        return n
    return fibo_recurtion(n - 1) + fibo_recurtion(n - 2)

n = int(input('input n: '))
for i in range(n):
    print(fibo_recurtion(i), end= ' ')


def fibo_list(n, fib_1 = 0, fib_2 = 1, fib_lst = [0]):
    if n == 1:
        return fib_lst
    else:
        fib_lst.append(fib_1 + fib_2)
        return fibo_list(n - 1, fib_1 + fib_2, fib_1, fib_lst)

print(fibo_list(10))