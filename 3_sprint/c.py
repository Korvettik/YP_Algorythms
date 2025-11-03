from collections import deque

def common_logic(first_string_s_deque, first_string_s_count, second_string_t_deque):

    # базовый случай
    if first_string_s_count == 0:
        print('True')
        return  # выход

    else:
        first_letter = first_string_s_deque.popleft()  # вырезали левый

        # проходимся по всем элементам 2 строки
        while second_string_t_deque:
            second_letter = second_string_t_deque.popleft()
            if second_letter == first_letter:
                first_string_s_count -= 1
                common_logic(first_string_s_deque, first_string_s_count, second_string_t_deque)







first_string_s = input()
second_string_t = input()

first_string_s_deque = deque(first_string_s)  # на основе итерируемого объекта создаем скоростной дек
second_string_t_deque = deque(second_string_t)  # на основе итерируемого объекта создаем скоростной дек
first_string_s_count = len(first_string_s)

common_logic(first_string_s_deque, first_string_s_count, second_string_t_deque)