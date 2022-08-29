from math import pi


def circle_squer(radius) -> float:
    squer = pi * radius ** 2
    return f'{squer:.2f}'


def circle_perimetr(radius) -> float:
    perimetr = 2 * pi * radius
    return f'{perimetr:.2f}'
