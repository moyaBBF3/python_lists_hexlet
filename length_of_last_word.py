def length_of_last_word(string):
    '''
    Функция возвращает длину последнего слова.
    словом считается любая последовательность,
    не содержащая пробелов
    '''
    result = string.rstrip().split(' ')
    return len(result[-1])


first_str = ' '
second_str = 'I feel progress'
third_str = 'it\'s simple                         '
print(length_of_last_word(first_str))
print(length_of_last_word(second_str))
print(length_of_last_word(third_str))

