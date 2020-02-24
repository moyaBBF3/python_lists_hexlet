def find_index(value, items):
    '''
    Функция принимает значение и нечто, по чему можно 
    итерироваться — строку, список, кортеж. В ответ 
    функция должна вернуть индекс первого элемента 
    итерируемой последовательности, равного заданному 
    значению. Если же значение в последовательности не 
    встречается или же последовательность окажется 
    пустой, функция должна вернуть None.
    '''
    for index, item in enumerate(items):
        if item == value:
            return index


print(find_index(1, []))
print(find_index(5, [1, 3, 5, 7, 9]))
print(find_index('u', 'Wonderful'))
print(find_index(2, [1, 3, 5, 7, 9]))
print(find_index('k', 'Next stage'))
