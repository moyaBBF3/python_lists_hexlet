def chunked(divider, sequence):
    '''
    Функция принимает на вход число и последовательность.
    Число задаёт размер чанка (куска). Функция возвращает 
    список, состоящий из чанков указанной размерности.
    '''
    index = 0
    result = []
    while index < len(sequence):
        result.append(sequence[index:index + divider])
        index += divider
    return result


print(chunked(4, []))
print(chunked(2, ['one']))
print(chunked(2, ['one', 'two', 'three', 'four']))
print(chunked(3, 'ABCD'))
print(chunked(2, (1, 2, 3, 4)))
