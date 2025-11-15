# https://contest.yandex.ru/contest/24414/run-report/148625649/

# -- ПРИНЦИП РАБОТЫ ---
# Решил делать хэш таблицу на основе метода цепочек
# Создаем объект - таблица. В ней первым делом создаем пустой список списков.
# Размер его 10**5 (по условию задачи). Структура таблицы сделана так - если подается ключ,
# то мы его переводим в хэш индекс. По данному хэш-индексу получаем доступ к списку-хранилищу (коробке)
# всех пар-значений (которые тоже являются мини-списками ключ-значение).
# Перебираем в этой коробке существующие мини-списки и если там есть пара, где первый элемент (изначальный индекс) соответствует вновь записываемому - мы меняем значение. Если нет - записываем новый мини-список (пару).
# Получение и удаление работает по аналогичному принципу


# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --
# Реализованный метод не использует встроенный объект dict, но реализует схожий функционал


# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --
# Временная сложность --- все операции выполняются за O(1) в среднем, т.к. идет прямое обращение к индексу элемента, который получаем как хэш-ключ от подаваемого ключа
# Пространственная сложность равна O(n) --- так как мы работаем с теми данными, что кладем в список и их нужно хранить.


class Table():
    def __str__(self):
        """Класс хэш таблицы"""

    def __init__(self):
        self.table = [list() for _ in range(10**5)]  # массив пустых списков, максимальный размер таблицы и индексов
        #print(self.table[:5])

    def put(self, key, value):
        # добавление пары ключ-значение. Если заданный ключ
        # уже есть в таблице, то соответствующее ему значение обновляется"
        #print(f'put, {key}, {value}')
        index_hash = self.make_index(key)  # создаем новый ключ для хэш-таблицы
        box_list = self.table[index_hash]

        # теперь анализируем саму коробку (локальный список)
        # для этого проходимся по внутренним парам ключ-значение,
        box_list_len = len(box_list)
        for i in range(box_list_len):
            if box_list[i][0] == key:  # есть такая пара с таким ключем
                #print(f'box_list[i] {box_list[i]}')
                box_list[i][1] = value  # меняем значение
                return
        # ключа не было, значит просто добавляем
        box_list.append([key, value])





    def get(self, key):
        # получение значения по ключу. Если ключа нет в таблице,
        # то вывести «None». Иначе вывести найденное значение.
        #print(f'get, {key}')
        #print(f'get key{key} --- value {value}')
        index_hash = self.make_index(key)  # вычисляем ключ для хэш-таблицы
        box_list = self.table[index_hash]
        for k, v in box_list:
            if k == key:
                print(v)
                return
        # если ключа нет
        print(None)


    def delete(self, key):
        # удаление ключа из таблицы. Если такого ключа нет, то вывести «None»,
        # иначе вывести хранимое по данному ключу значение и удалить ключ.
        #print(f'delete, {key}')
        index_hash = self.make_index(key)  # вычисляем ключ для хэш-таблицы
        box_list = self.table[index_hash]
        box_list_len = len(box_list)
        for i in range(box_list_len):
            if box_list[i][0] == key:  # есть такая пара с таким ключем
                print(box_list[i][1])
                del box_list[i] # удаляем пару значение
                return
        print(None)





    def make_index(self, key):
        # по ключу делает хэш-индекс для списка  (новый индекс)
        index_hash = abs(hash(key)) % 10**5
        #print(f'index_hash {index_hash}')
        return index_hash





if __name__ == '__main__':

    table = Table()

    n = int(input().strip())  # количество команд

    for i in range(n):
        command = input().strip().split(' ')
        if command[0] == 'put':
            table.put(key=int(command[1]), value=int(command[2]))
        elif command[0] == 'get':
            table.get(key=int(command[1]))
        elif command[0] == 'delete':
            table.delete(key=int(command[1]))

