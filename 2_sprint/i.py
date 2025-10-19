class Data:
    def __str__(self):
        """класс хранения данных"""

    def __init__(self):
        self.max_size_commands = None
        self.queue_size = None
        self.commands_list = None


class MyQueueSized:
    def __str__(self):
        """класс стэка"""

    def __init__(self, max_size_commands, queue_size):
        self.max_size_commands = max_size_commands
        self.queue_size = queue_size
        self.elements = list()


    def push(self, x):
        "добавить число x в очередь"
        "При превышении допустимого размера очереди нужно вывести «error»"
        if self.size() + 1 > self.queue_size:
            print('error')
        else:
            self.elements.append(x)
            print(x)

    def pop(self):
        "удалить число из очереди и вывести на печать"
        "для пустой очереди нужно вывести «None»"
        if self.size() > 0:
            res_pop = self.elements.pop()
            print(res_pop)
        else:
            print('None')

    def peek(self):
        "напечатать первое число в очереди"
        "для пустой очереди нужно вывести «None»"
        if self.size() > 0:
            res_peek = self.elements[-1]
            print(res_peek)
        else:
            print('None')

    def size(self):
        "вернуть размер очереди"
        res_size = len(self.elements)
        return res_size


def read_input():
    """получаем данные задачи из стандартного ввода"""
    max_size_commands = int(input())  # количество команд
    queue_size = int(input())  # размер очереди

    commands_list = list()

    for _ in range(max_size_commands):
        commands_list.append(input().strip())

    return max_size_commands, queue_size, commands_list





if __name__ == '__main__':
    """функция точки входа общей логики"""

    # создаем объект хранения данных
    data = Data()

    # теперь храним данные в объекте
    data.max_size_commands, data.queue_size, data.commands_list = read_input()

    my_queue_sized = MyQueueSized(data.max_size_commands, data.queue_size)

    for command in data.commands_list:
        if command == 'size':
            my_queue_sized.size()
        elif 'push' in command:
            my_queue_sized.push(int(command[5:]))
        elif command == 'pop':
            my_queue_sized.pop()
        elif command == 'peek':
            my_queue_sized.peek()
