import math


def triangle_squer(side_a, side_b, side_c):
    p = (side_a + side_b + side_c) / 2
    squer = math.sqrt(p * (p - side_a) * (p - side_b) * (p - side_c))
    return f'{squer:.2f}'


def triangle_perimetr(side_a, side_b, side_c):
    perimetr = side_a + side_b + side_c
    return perimetr
