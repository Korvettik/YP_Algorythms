

# -- ПРИНЦИП РАБОТЫ ---



# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --



# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --


class Queue:
    def __str__(self):
        """класс стек"""

    def __init__(self):
        self.queue = list()  # элементы очереди --- ОБЫЧНЫЙ СПИСОК
        self.first = None
        self.second = None


    def push(self, x):
        """добавить число x в стек"""
        #print(f'push {x} {type(x)}')
        self.queue.append(x)

    def pop(self):
        """взять число с вершины стека"""
        #print('pop')
        return self.queue.pop()

    def logic(self, command):
        """логика работы с арифметикой"""
        #print('logic')
        self.second = self.pop()
        self.first = self.pop()

        if command == '+':
            self.push(self.first + self.second)
        elif command == '-':
            self.push(self.first - self.second)
        elif command == '*':
            self.push(self.first * self.second)
        elif command == '/':
            self.push(self.first // self.second)

    def digit_check(self, command):
        """проверка, является ли строка числом, даже отрицательным"""
        try:
            int(command)
            return True
        except ValueError:
            return False



if __name__ == '__main__':

    queue = Queue()

    commands_list = input().strip().split()  # читаем символы нотации на вводе
    #print(commands_list)

    for command in commands_list:
        if queue.digit_check(command):
            #print('это цифра')
            queue.push(int(command))
        else:
            queue.logic(command)

    print(queue.pop())