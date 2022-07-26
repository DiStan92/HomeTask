'''task_3
count element in list'''

import random

def create_list():
    lst_gen = [random.randint(1, 100) for i in range(101)]
    print(lst_gen)
    return lst_gen

def count_element(lst: list) -> dict:
    count_dict = {}
    for ls in lst:
        count_dict[ls] = lst.count(ls)
    print(count_dict)
    return count_dict

def pr(dct: dict):
    for el, count in dct.items():
        print(f'{el} - {count}')

pr(count_element(create_list()))