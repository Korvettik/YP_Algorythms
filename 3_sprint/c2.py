def common_logic(first_string_s, second_string_t):

    # базовый случай
    if len(first_string_s) == 0:
        return True  # выход

    # если выше не вывалились. то переходим сюда. а здесь значит, что строка закончилась
    if len(second_string_t) == 0:
        return False


    index = 0
    current = first_string_s[index]

    for letter in second_string_t:
        if letter == current:
            # сдвигаем индекс для первой строки
            index += 1

            # проверка, что раз последний индекс совпадает как число с количеством элементов
            if len(first_string_s) == index:
                return True

            # получаем новый элемент для первой строки по сдвинутому индексу
            current = first_string_s[index]

    return False




first_string_s = input().strip()
second_string_t = input().strip()


result = common_logic(first_string_s, second_string_t)
print(result)

