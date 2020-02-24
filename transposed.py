def transposed(sequence):
    '''
    Функция принимает матрицу в виде списка списков
    и возвращает новый список списков - транспортированную
    матрицу.
    '''
    return list(map(list, zip(*sequence)))


first_matrix = [[1, 2], [3, 4]]
second_matrix = [[1, 2], [3, 4], [5, 6]]
third_matrix = [['d', 'o'], ['r', 'e'], ['m', 'i']]
print(transposed(first_matrix))
print(transposed(second_matrix))
print(transposed(third_matrix))
