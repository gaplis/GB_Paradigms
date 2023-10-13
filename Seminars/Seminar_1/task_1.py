# Задание 1:

# Контекст:
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.

# Задача:
# Реализовать императивную функцию поиска элементов на языке Python

def search(lst, targ):
    for i in lst:
        if i == targ:
            return True
    return False


init_list = [1, 2, 3, 4, 5]
target = 11
print(search(init_list, target))

# Контекст:
# Предположим, что нам хочется для любого массива чисел array и любого числа target узнать содержится
# ли target в array. Такую процедуру будем называть поиском.

# Задача:
# Реализовать декларативную функцию поиска элементов на языке Python.


def search_declarative(array, targ):
    return targ in array
