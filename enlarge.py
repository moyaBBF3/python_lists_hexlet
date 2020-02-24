def enlarge(image):
    '''
    Функция принимает изображение в виде двумерного списка строк
    и увеличивает его в два раза: удваивает каждый симол  по
    горизонтали и вертикали.
    '''
    result = []
    for element in image:
        str_result = ''
        for value in element:
            value += value
            str_result += value
        result.append(str_result)
        result.append(str_result)
    return result


first_pic = ['@']
second_pic = ['_*', '#_']
print(enlarge(first_pic))
print()
print(enlarge(second_pic))
