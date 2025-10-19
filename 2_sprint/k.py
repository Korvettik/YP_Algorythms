class Data:
    def __init__(self):
        self.n = None
        self.counter_flag = 0

        self.first = None
        self.second = None

        self.result_commit_count = 1



def read_input():
    """получаем данные задачи из стандартного ввода"""
    n = int(input())  # целое число
    return n






def recursion_logic():
    """логика рекурсивного прохождения по элементам"""

    if data.n >= 0:

        if data.counter_flag == 0:
            #print('data.counter_flag == 0')
            data.counter_flag += 1
            data.first = 1
            data.n -= 1
            recursion_logic()

        elif data.counter_flag == 1:
            #print('data.counter_flag == 1')
            data.counter_flag += 1
            data.second = 1
            data.n -= 1
            recursion_logic()

        else:
            #print('data.counter_flag')
            data.counter_flag += 1
            first = data.first
            second = data.second
            #print(f'first {first}, second {second}')
            data.result_commit_count = first + second
            new_second = data.result_commit_count

            data.first = second
            data.second = new_second

            data.n -= 1
            recursion_logic()

    else:
        return







# 0-1
# 1-1
# 2-2
# 3-3
# 4-5
# 5-8
# 6-13




if __name__ == '__main__':
    """функция точки входа общей логики"""

    data = Data()
    data.n = read_input()

    recursion_logic()

    print(data.result_commit_count)

