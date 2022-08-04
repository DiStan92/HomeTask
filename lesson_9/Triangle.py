from random import random

class Triangle:
    def __init__(self, side_lst):
        for i in range(len(side_lst)):
            if str(side_lst[i]).isdigit():
                self.side_lst = side_lst
            else:
                return 'error'

    def build_triangle(self):
        self.side_lst.sort()
        if self.side_lst[0] + self.side_lst[1] > self.side_lst[2]:
            return print('triangle is build')
        else:
            return print('triangle is not build')
            
def create_side_init(n=3):
    side_lst = [int(random()*100) for _ in range(n)]
    print(side_lst)
    return side_lst

triangle_1 = Triangle(create_side_init())

triangle_1.build_triangle()
