# Задание 3:
#
# Контекст:
# Ещё один известный и довольно эффективный алгоритм
# сортировки массива - сортировка слиянием (merge sort).
# Алгоритм делится на два этапа:
# ○ этап разбиения - массив разбивается на пару
# массивов до тех пор пока, полученные массивы не
# станут массивами длины 1 (состоящими из одного
# элемента).
# ○ этап слияния - соединяем пары массивов в большие
# массивы так, чтобы полученные массивы были
# отсортированы.
#
# Ваша задача:
# Реализовать сортировку слиянием на любом языке в любой
# парадигме. На вход ваша программа получает массив из
# чисел, а вернуть должна отсортированный массив.


def sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = arr[:middle]
    right = arr[middle:]
    left = sort(left)
    right = sort(right)
    return merge(left, right)


def merge(left, right):
    result = []
    left_index = 0
    right_index = 0
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    result += left[left_index:]
    result += right[right_index:]
    return result


array = [6, 17, 19, 1, 15, 4, 3]
print(sort(array))
