class Node:
    """Элемент очереди"""

    def __init__(self):
        self.value = None
        self.next_item = None








class DoubleStack:
    def __str__(self):
        """класс связный список - сама очередь"""

    def __init__(self):
        self.head_node = None  # возвращаемая  голова
        self.counter = 0  # счетчик глубины связного списка
        self.tail_node = None  # самый последний узел

    def size(self):
        "вернуть размер очереди"
        print(self.counter)

    def put(self, x):
        "добавить число x в очередь"

        # создали новый узел, пока независимый
        node = Node()
        node.value = x

        # увязываем его с существующими
        if self.counter == 0:
            self.head_node = node
            self.tail_node = node
        else:
            # нужно найти последний элемент

            current_tail = self.tail_node  # берем текущий хвост
            current_tail.next_item = node  # соединили с новым элементом
            self.tail_node = node  # положили новый элемент как конец цепи

        #print(f'положили {self.head_node.value}')
        self.counter += 1  # увеличили глубину списка


    def get(self):
        # "вывести элемент, находящийся в голове очереди,
        # и удалить его.
        # Если очередь пуста, то вывести «error»."

        if self.counter > 0:
            print(self.head_node.value)  # выводим значение головы
            self.counter -= 1  # уменьшаем глубину

            next_node = self.head_node.next_item  # получили следующий элемент
            self.head_node.next_item = None  # текущий никуда не ведет
            self.head_node = next_node  # передвинули голову

        else:
            print('error')







    # def recursion_logic(self, node):
    #     """логика рекурсивного прохождения по элементам очереди - в самый конец"""
    #     if node.next_item is not None:
    #         self.recursion_logic(node.next_item)
    #     else:
    #         return node









def read_input():
    """получаем данные задачи из стандартного ввода"""
    n = int(input())  # количество команд

    for _ in range(n):
        command = input().strip()

        if command == 'size':
            doublestack.size()
        elif 'put' in command:
            doublestack.put(int(command[4:]))
        elif command == 'get':
            doublestack.get()


if __name__ == '__main__':
    """функция точки входа общей логики"""

    # создаем объект головы связного списка
    doublestack = DoubleStack()

    read_input()


