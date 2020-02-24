def same_parity_filter(sequence):
    '''
    Функция принимает список и возвращает новый
    список, состоящий из элементов, у которых
    такая же чётность, как и у первого элемента
    исходного списка.
    '''
    remainder = sequence[0] % 2
    result = []
    for element in sequence:
        if element % 2 == remainder:
            result.append(element)
    return result


first_list = [2, 0, 1, -3, 10, -2] # [2, 0, 10, -2]
second_list = [10, -1.5, 1.3, -3, 25, -2] # [10, -2]
third_list = [-1, 0, 1, -3, 10, -2] # [-1, 1, -3]
print(same_parity_filter(first_list))
print(same_parity_filter(second_list))
print(same_parity_filter(third_list))
