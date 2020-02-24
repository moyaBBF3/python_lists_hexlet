# Функции принимают аргумент: список, кортеж или строка. 
# С помощью срезов и конкатенации получает новое значение 
# такого же типа и возвращает его.


def rotated_left(value):
    '''
    При вращении влево первый элемент перемещается в конец.
    '''
    return value[1:] + value[:1]


def rotated_right(value):
    '''
    При вращении вправо последний элемент перемещается в начало.
    '''
    return value[-1:] + value[:-1]


my_sting = 'ABCDEF'
my_list = [0, 1, 2, 3, 4, 5]
my_tuple = ('zero', 1, 'two', None)
print(rotated_left(my_sting))
print(rotated_left(my_list))
print(rotated_left(my_tuple))
print()
print(rotated_right(my_sting))
print(rotated_right(my_list))
print(rotated_right(my_tuple))
