class Data:
    def __str__(self):
        """класс хранения данных"""

    def __init__(self):
        self.n = None
        self.commands_list = None


class StackMaxEffective:
    def __str__(self):
        """класс стэка максимально эффективный"""

    def __init__(self):
        self.elements = list()

    def push(self, x):
        """добавить число x в стек"""
        self.elements.append(x)

    def pop(self):
        """удалить число с вершины стека"""
        # Если стек пуст напечатать «error».
        if len(self.elements) == 0:
            print('error')
        else:
            self.elements.pop()

    def get_max(self):
        """напечатать максимальное число в стеке"""
        # Если стек пуст нужно напечатать «None»
        if len(self.elements) == 0:
            print('None')
        else:
            print(max(self.elements))

    def top(self):
        """"напечатать число с вершины стека"""
        # Если стек пуст напечатать «error».
        if len(self.elements) == 0:
            print('error')
        else:
            print(self.elements[-1])


def read_input():
    """получаем данные задачи из стандартного ввода"""
    n = int(input())  # количество команд

    commands_list = list()
    for _ in range(n):
        commands_list.append(input().strip())

    #rint(commands_list)
    return n, commands_list


def solution():
    """функция точки входа общей логики"""
    import sys
    #print(sys.getrecursionlimit())  # Выводим существующий лимит рекурсии
    sys.setrecursionlimit(100000)  # новый лимит (по задачке)


    stack = StackMaxEffective()

    for command in data.commands_list:
        if command == 'get_max':
            stack.get_max()
        elif 'push' in command:
            stack.push(int(command[5:]))
        elif command == 'pop':
            stack.pop()
        elif command == 'top':
            stack.top()





if __name__ == '__main__':

    # создаем объект хранения данных
    data = Data()

    # теперь храним данные в объекте
    data.n, data.commands_list = read_input()

    solution()
