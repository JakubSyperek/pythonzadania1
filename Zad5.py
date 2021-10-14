def foo(x,y):
    if y == 0:
        print('Liczba nie może być równa zero!')
    elif x < 0 or y < 0:
        print('Liczby muszą być dodatnie.')
    else:
        print(x, '/', y, )