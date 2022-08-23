from circle import circle_squer, circle_perimetr
from triangle import triangle_squer, triangle_perimetr
from rectangle import rectangle_squer, rectangle_perimetr


def rectangle_res(rectangle_squer, rectangle_perimetr):
    return {'rectangle': {'squer': rectangle_squer, 'perimetr': rectangle_perimetr}}


def circle_res(circle_squer, circle_perimetr):
    return {'circe': {'squer': circle_squer, 'perimetr': circle_perimetr}}


def triangle_res(triangle_squer, triangle_perimetr):
    return {'triangle': {'squer': triangle_squer, 'perimetr': triangle_perimetr}}


def res_dict(rectangle_res, circle_res, triangle_res):
    return {**rectangle_res, **circle_res, **triangle_res}


print(rectangle_res(rectangle_squer(4, 5), rectangle_perimetr(4, 5)))
print(circle_res(circle_squer(5), circle_perimetr(5)))
print(triangle_res(triangle_squer(2, 4, 5), triangle_perimetr(2, 4, 5)))

print(
    res_dict(
        rectangle_res(rectangle_squer(4, 5), rectangle_perimetr(4, 5)),
        circle_res(circle_squer(5), circle_perimetr(5)),
        triangle_res(triangle_squer(2, 4, 5), triangle_perimetr(2, 4, 5))
    )
)
