from random import random


def create_rand_list(len_list: int) -> list:
    rand_list = [int(random()*100) for _ in range(len_list)]
    return  rand_list


def counter(random_list: list) -> set:
    print(random_list)
    count_lst = [random_list.count(x) for x in random_list]
    print(count_lst)
    lst = set((i, n) for i, n in zip(random_list, count_lst) if n > 1)
    return lst

print(counter(create_rand_list(10)))

