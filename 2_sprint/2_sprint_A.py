
class Queue:
    def __str__(self):
        """класс очередь на кольцевом буфере"""

    def __init__(self, m):
        self.queue = [None] * m   # элементы очереди --- ОБЫЧНЫЙ СПИСОК
        self.head = 0  # индекс, по которому нужно извлекать элемент, если очередь не пустая;
        self.tail = 0  # индекс, по которому нужно добавлять элемент, если в очереди есть место;
        self.max_m = m  # максимально возможное количество элементов в очереди
        self.size = 0  # размер очереди


    def is_empty(self):
        return self.size == 0
    #
    #
    # def push(self, x):
    #     if self.size != self.max_n:
    #         self.queue[self.tail] = x
    #         self.tail = (self.tail + 1) % self.max_n
    #         self.size += 1
    #
    #
    # def pop(self):
    #     if self.is_empty():
    #         return None
    #     x = self.queue[self.head]
    #     self.queue[self.head] = None
    #     self.head = (self.head + 1) % self.max_n
    #     self.size -= 1
    #     return x


    # ------------------------------------------
    # добавить элемент в конец дека. Если в деке уже находится максимальное число элементов,
    # вывести «error».
    # Для успешных запросов push_back(x) и push_front(x) ничего выводить не надо.
    def push_back(self, value):
        if self.size != self.max_m:
            self.tail = (self.tail + 1) % self.max_m
            self.queue[self.tail] = value
            self.size += 1
        else:
            print('error')




    # добавить элемент в начало дека. Если в деке уже находится максимальное число элементов, ======== все верно, движемся в обратном направлении
    # вывести «error».
    def push_front(self, value):
        if self.size != self.max_m:
            self.head = (self.head - 1) % self.max_m
            self.queue[self.head] = value
            self.size += 1
        else:
            print('error')


    # вывести первый элемент дека и удалить его. Если дек был пуст, то вывести «error».
    def pop_front(self):
        if self.is_empty():
            print('error')
        x = self.queue[self.head]
        self.head = (self.head + 1) % self.max_m
        self.queue[self.head] = None
        self.size -= 1
        print(x)


    # вывести последний  элемент дека и удалить его. Если дек был пуст, то вывести «error». ====================
    def pop_back(self):
        if self.is_empty():
            print('error')
        self.tail = (self.tail - 1) % self.max_m
        x = self.queue[self.tail]
        self.queue[self.tail] = None
        self.size -= 1
        print(x)


if __name__ == '__main__':
    n = int(input())  # количество команд
    m = int(input())  # максимальный размер дека

    queue = Queue(m)

    for _ in range(n):
        command = input().strip().split()

        if command[0] == 'push_back':
            print(command)
            queue.push_back(command[1])
            print(queue.queue)
            print()
        elif command[0] == 'push_front':
            print(command)
            queue.push_front(command[1])
            print(queue.queue)
            print()
        elif command[0] == 'pop_front':
            print(command)
            queue.pop_front()
            print(queue.queue)
            print()
        elif command[0] == 'pop_back':
            print(command)
            queue.pop_back()
            print(queue.queue)
            print()

    # print(queue.queue)


# 4
# 4
# push_back 1
# push_back 2
# push_front 3
# push_front 4


# 4
# 4
# push_front 861
# push_front -819
# pop_back
# pop_back