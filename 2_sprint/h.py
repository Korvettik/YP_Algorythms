
class Stack:
    def __str__(self):
        """класс стэка"""

    def __init__(self):
        self.elements = list()

    def push(self, x):
        """добавить число x в стек"""
        self.elements.append(x)

    def pop(self):
        """удалить число с вершины стека"""
        #Если стек пуст напечатать «error».
        if len(self.elements) == 0:
            return None
        else:
            self.elements.pop()

    def get_top(self):
        """показать вершину стека"""
        #Если стек пуст напечатать «error».
        if len(self.elements) == 0:
            return None
        else:
            item = self.elements[-1]
            return item

    def get_len(self):
        "показать количество элементов стека"
        return len(self.elements)






def is_correct_bracket_seq(instance):
    """функция принимает скобочную последовательность"""
    # базово, чтобы ключи были и пары нужные

    stack = Stack()

    for item in instance:
        if item in ('(', '{', '['):
            stack.push(item)

        else:  # (')', '}', ']')
            if item == ')':
                if stack.get_top() == '(':
                    stack.pop()
                else:
                    return False

            elif item == '}':
                if stack.get_top() == '{':
                    stack.pop()
                else:
                    return False

            elif item == ']':
                if stack.get_top() == '[':
                    stack.pop()
                else:
                    return False

    if stack.get_len() == 0:
        return True
    else:
        return False










instance = input().strip()
res = is_correct_bracket_seq(instance)
print(res)