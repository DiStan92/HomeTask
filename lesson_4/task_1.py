'''task_1
lcm'''

def lcm(a: int, b: int) -> int:
    m = max(a, b)
    while True:
        if m % a == 0 and m % b == 0:
            break
        else: m += 1
    return m

num_1 = int(input('input num1: '))
num_2 = int(input('input num2: '))
print(f'lcm for {num_1, num_2} is {lcm(num_1, num_2)}')