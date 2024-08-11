def divide(first, second):
    while True:
        try:
            first / second
            if second > 0:
                return first / second
        except ZeroDivisionError:
            return 'Ошибка'
