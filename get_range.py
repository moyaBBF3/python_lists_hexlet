def get_range(number):
    '''
    Функция для заданного положительного числа аргумента
    возвращает список чисел от нуля до аргумента, не включая его.
    Если будет передан ноль или отрицательное число, вернуть 
    пустой список.
    '''
    counter = 0
    result = []
    while counter < number:
        result.append(counter)
        counter += 1
    return result


print(get_range(-10))
print(get_range(0))
print(get_range(10))
