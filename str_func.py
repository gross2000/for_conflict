def cap_lit(instring):

    """ функция для возвращения строки пользователя заглавными буквами, строка для конфликта"""
    return instring.upper()

def first_cap(instring):

    """ функция для возврата строки пользователя со словами с первой заглавной буквой"""
    words = instring.split()
    cap_words = [word.capitalize() for word in words]
    return ''.join(cap_words)
