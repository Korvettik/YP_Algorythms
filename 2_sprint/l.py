class Data:
    def __init__(self):
        self.n = None
        self.k = None

        self.counter_flag = 0

        self.first = None
        self.second = None

        self.result_commit_count = 1



def read_input():
    """получаем данные задачи из стандартного ввода"""
    n, k = list(map(int, input().strip().split()))  # целые числа
    return n, k






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

            # МНОГО ПАМЯТИ, НО БЫСТРО

            # first = data.first
            # second = data.second
            # data.result_commit_count = first + second
            # new_second = data.result_commit_count
            #
            # data.first = second
            # data.second = new_second


            # МАЛО ПАМЯТИ, НО ЧУТЬ ПОДОЛЬШЕ

            data.result_commit_count = data.first + data.second
            data.first = data.second
            data.second = data.result_commit_count

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

    import sys
    sys.setrecursionlimit(1000000)  # новый лимит (по задачке) для рекурсии


    data = Data()
    data.n, data.k = read_input()

    #print(data.n, data.k)

    recursion_logic()

    k_new = data.k
    for _ in range(data.k):
        k_new *= 10
        #print(k_new)
    res = data.result_commit_count % k_new
    #print(f'res {res}')

    new_res_string = ''
    flag = False
    str_res = str(res)
    len_res = len(str_res)
    if len_res > data.k:
        start = len_res - data.k

        for letter in str_res[start:]:
            if letter == '0' and flag is False:
                pass
            else:
                new_res_string += letter
                flag = True
        print(int(new_res_string))

    else:
        print(res)



