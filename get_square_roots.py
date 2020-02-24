import math


def get_square_roots(number):
    '''
    Функция принимает число и возвращает список квадратных корней.
    Например, для аргумента 25 функция вернёт [-5, 5].
    Корень может быть один, если аргумент равен нулю.
    Если аргумент отрицательный, то корней не будет.
    '''
    if number < 0:
        return []
    elif number:
        root = math.sqrt(number)
        return [-root, root]
    return [0]


print(get_square_roots(0))
print(get_square_roots(-10))
print(get_square_roots(1024))
