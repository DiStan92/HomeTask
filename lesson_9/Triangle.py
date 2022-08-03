class Triangle:
    def __init__(self, side_lst):
        self.side_lst = side_lst

    def true_false(self):
        self.side_lst.sort()
        if self.side_lst[0] + self.side_lst[1] > self.side_lst[2]:
            return print('triangle is true')
        else:
            return print('triangle is false')

def create_side_list(n = 3):
    side_lst = []
    for i in range(n):
        side = int(input('input side '))
        side_lst.append(side)
    return side_lst

triangle_1 = Triangle(create_side_list())
triangle_1.true_false()

triangle_2 = Triangle(create_side_list())
triangle_2.true_false()
