# Задание 1:
#
# Контекст:
# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
#
# Ваша задача:
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.


from statistics import correlation, mean

lst1 = [1, 2, 3, 4, 5]
lst2 = [5, 4, 3, 2, 1]


def my_correlation(x, y):
    avg_x = mean(x)
    avg_y = mean(y)

    return sum(list(map(lambda ix, iy: (ix - avg_x) * (iy - avg_y), x, y))) \
        / (sum(list(map(lambda ix: (ix - avg_x) ** 2, x))) * (sum(list(map(lambda iy: (iy - avg_y) ** 2, y))))) ** 0.5


print(my_correlation(lst1, lst2))
print(correlation(lst1, lst2))
