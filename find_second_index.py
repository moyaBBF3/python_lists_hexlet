def find_second_index(value, items):
    '''
    Функция возвращает индекс второго подходящего
    элемента в последовательности.Если подходящих 
    элементов в последовательности меньше двух 
    или же последовательность пуста, нужно 
    возвращать None.
    
    '''
    result = []
    for index, item in enumerate(items):
        if item == value:
            result.append(index)
    try:
        return result[1]
    except IndexError:
        return None


print(find_second_index('s', 'odysseus'))
print(find_second_index('o', 'Yoshi'))
