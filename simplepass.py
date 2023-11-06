from random import randint
def password_generator(num:int):
    letters = 'qwertyuiopasdfghjklzxcvbnm'
    data = [[i for i in letters.upper()],[i for i in letters],[i for i in '12345678901234567890+-*/$&']]
    result =[]
    for i in range(num):
        result.append(data[randint(0,2)][randint(0,25)])
    return ''.join(result)

