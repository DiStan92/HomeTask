'''task 2
выводит все элементы первого,
 которых нет во втором'''

lst_1 = input('Input list_1: ').split(', ')
lst_2 = input('Input list_2: ').split(', ')
print(f'element {set(lst_1).difference(set(lst_2))} not in list 2')

