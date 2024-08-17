def test_function():
    print('Я внешняя функция') #если удалить эту строчку и/или под номером 9 (test_function()), то ничего выводиться не будет

    def inner_function():
        print("Я в области видимости функции test_function")

    inner_function()

test_function()
inner_function() #вне функции выдает ошибку
