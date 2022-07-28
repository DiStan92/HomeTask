'''task 1
number is simple or add'''

num = int(input('Input num 0-1000: '))
amount = 0
for n in range(2, num // 2 + 1):
    if num % n == 0:
        amount += 1
if amount == 0:
    print(f'{num} is simple')
else: print(f'{num} is not simple')
