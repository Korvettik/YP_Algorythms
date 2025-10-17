class Data:
    def __str__(self):
        """класс хранения данных"""

    def __init__(self):
        self.n = None
        self.commands_list = list()


class StackMaxEffective:
    def __str__(self):
        """класс стэка максимально эффективный"""

    def __init__(self):
        self.elements = list()

    def push(self, x):
        """добавить число x в стек"""
        if len(self.elements) == 0:
            self.elements.append((x,x,))  # каждый элемент это кортеж
        else:
            if x > self.elements[-1][1]:  # обновляем максимум
                self.elements.append((x,x,))
            else:
                self.elements.append((x,self.elements[-1][1],))


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
            print(self.elements[-1][1])

    def top(self):
        """"напечатать число с вершины стека"""
        # Если стек пуст напечатать «error».
        if len(self.elements) == 0:
            print('error')
        else:
            print(self.elements[-1][0])


def read_input(stack):
    """получаем данные задачи из стандартного ввода"""
    n = int(input())  # количество команд

    for _ in range(n):
        command = input().strip()

        if command == 'get_max':
            stack.get_max()
        elif 'push' in command:
            stack.push(int(command[5:]))
        elif command == 'pop':
            stack.pop()
        elif command == 'top':
            stack.top()


def solution():
    """функция точки входа общей логики"""
    import sys
    #print(sys.getrecursionlimit())  # Выводим существующий лимит рекурсии
    sys.setrecursionlimit(100000)  # новый лимит (по задачке)

    stack = StackMaxEffective()

    read_input(stack)






if __name__ == '__main__':

    # создаем объект хранения данных
    data = Data()

    # # теперь храним данные в объекте
    # data.n, data.commands_list = read_input()

    solution()
