num_1 = list(input('Input number1, number2: ').split(', '))
print(num_1, num_1[1])
lst = []
amount = 0
for i in range(int(num_1[0]), int(num_1[1])+1):
    lst.append(i)
    if i % 5 != 0:
        amount += 1
print(f'list - {lst}\namount - {amount}')