from random import random

class Triangle:
    def __init__(self, side_lst):
        if len(side_lst) == 3:
            self.side_lst = side_lst
        else:
            self.side_lst = None
    def build_triangle(self):
        if self.side_lst is not None:
            print(self.side_lst)
            self.side_lst.sort()
            if self.side_lst[0] + self.side_lst[1] > self.side_lst[2]:
                return print('triangle is build')
            else:
                return print('triangle is not build')
        else:
            return print('incorrect data')
def create_side_list(n = 3):
    side_lst = [int(random()*100) for _ in range(n)]
    print(side_lst)
    return side_lst
def create_side(n = 3, side_lst = []):
    for i in range(1, n + 1):
        i = input(f'input side_{i}: ')
        if i.isdigit():
            side_lst.append(int(i))
        else:
            print('error')
    return side_lst

triangle_1 = Triangle(create_side_list())
triangle_1.build_triangle()

triangle_2 = Triangle(create_side())
triangle_2.build_triangle()
