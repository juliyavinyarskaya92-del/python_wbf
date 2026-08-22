from math import ceil


def square(side):
    area = side * side
    return ceil(area)


result = square(2.5)

print(result)
