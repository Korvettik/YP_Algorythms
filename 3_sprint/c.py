from collections import deque


def common_logic(first_string_s_deque, first_string_s_count, second_string_t_deque):

    # базовый случай
    if first_string_s_count == 0:
        #print('True')
        return True  # выход

    else:
        first_letter = first_string_s_deque.popleft()  # вырезали левый

        # проходимся по всем элементам 2 строки
        while second_string_t_deque:
            second_letter = second_string_t_deque.popleft()

            if second_letter == first_letter:
                first_string_s_count -= 1
                result = common_logic(first_string_s_deque, first_string_s_count, second_string_t_deque)

                # если это был последний заход в рекурсию и он был достаточным и успешным
                # Т.е. True передается обратным ходом по всей цепочке рекурсий
                if result is True:
                    return True

        # если обратным рекурсивным ходом не получили True и не вышли, то упадем сюда
        return False




first_string_s = input()
second_string_t = input()

first_string_s_deque = deque(first_string_s)  # на основе итерируемого объекта создаем скоростной дек
second_string_t_deque = deque(second_string_t)  # на основе итерируемого объекта создаем скоростной дек
first_string_s_count = len(first_string_s)


result = common_logic(first_string_s_deque, first_string_s_count, second_string_t_deque)
print(result)

