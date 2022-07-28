'''task3
colculation from str'''

st = input('Input example: ').split()
lst = ['+', '-', '*', '/']
if lst.index(st[1]) == 0:
    print(f'result = {int(st[0]) + int(st[2])}')
elif lst.index(st[1]) == 1:
    print(f'result = {int(st[0]) - int(st[2])}')
elif lst.index(st[1]) == 2:
    print(f'result = {int(st[0]) * int(st[2])}')
elif lst.index(st[1]) == 3:
    print(f'result = {int(st[0]) / int(st[2])}')
else: print('Error')
