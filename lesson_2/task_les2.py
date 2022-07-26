"""задача 1"""
stroka  = input('input num:')
print(f'stroka {stroka.strip(",. ")} \nspisok - {stroka.strip(",. ").split(", ")} \
      \ntuple - {tuple(stroka.strip(",. ").split(", "))}')

"""задача 2"""
num = int(input('Input number: '))
if num % 2 == 0:
   print(f'{num} Четное')
else: print(f'{num} нечетное')

"""задача 3"""
x = int(input('input x: '))
y = int(input('input y: '))
print(f'x={x}, y={y}')
x, y = y, x
print(f'x={x}, y={y}')

"""задача 4"""
st = input('input str: ')
if len(st) > 2:
    print(st[1:-1])
elif len(st) == 2:
    print(None)
else: print('Error')