# не сами пишем, а импортируем существующий встроенный метод
# создания объекта ДЕК - одновременно и стек и очередь
from collections import deque

buttons = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}


def word_generator(input_string_deque, result, line=''):

    # базовый случай - выход из рекурсии
    if len(input_string_deque) == 0:  # вырезаемые копии дека пусты
        #print(line)
        result.append(line)  # сохраняем собранную комбинацию
        return

    else:
        # берем и вырезаем слева дека элемент
        digit = int(input_string_deque.popleft())

        # по словарю, для каждой буквы этого элемента
        for char in buttons.get(digit):
            # рекурсивно используем эту же функцию, но передаем в нее
            # 1) копию уменьшенного слева дека
            # 2) общий результат
            # 3) накопительную букву

            word_generator(input_string_deque.copy(), result, line + char)

            # когда отработает рекурсия, мы снова вернемся в
            # предыдущую рекурсию внутрь ее цикла for, чтобы запустить
            # новую рекурсию






input_string = input().strip()  # то, что ввели
result = list()  # итоговый список
input_string_deque = deque(input_string)  # на основе итерируемого объекта создаем скоростной дек

#старт
word_generator(input_string_deque, result = result)

print(*result, sep=' ')


