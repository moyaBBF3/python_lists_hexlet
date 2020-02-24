def is_continuous_sequence(value):
    '''
    Функция проверяет, является ли последовательность
    целых чисел возрастающей непрерывно(не имеющей
    пропусков чисел). Последовательность может начинаться
    с любого числа.Последовательность из одного числа не 
    может считаться возрастающей.
    '''
    if len(value) < 2:
        return False
    for index, element in enumerate(value[1:]):
        if value[index] != (element - 1):
            return False
    return True


print(is_continuous_sequence([]))
print(is_continuous_sequence([100]))
print(is_continuous_sequence([-2, -1, 0, 1, 2]))
print(is_continuous_sequence([1011, 1012, 1013]))
