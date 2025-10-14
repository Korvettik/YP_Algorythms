from typing import List, Tuple

def get_sum(number_list: List[int], k: int) -> List[int]:
    # Здесь реализация вашего решения

    result = []

    k_list = list(map(int, (str(k))))[::-1]
    n_list = number_list[::-1]

    len_n_list = len(n_list)
    len_k_list = len(k_list)

    maximum_digits = max(len_n_list, len_k_list)

    if len_n_list > len_k_list:
        digits = len_n_list - len_k_list
        for _ in range(digits):
            k_list.append(0)
    else:
        digits = len_k_list - len_n_list
        for _ in range(digits):
            n_list.append(0)


    #print(f'k_list {k_list} n_list{n_list}')

    buffer = 0

    for i in range(maximum_digits):
        summ = k_list[i] + n_list[i] + buffer
        if summ < 10:
            result.append(summ)
            buffer = 0
        else:
            summ_digit = summ // 10
            #print(f'summ_digit {summ_digit}')
            buffer = summ_digit

            summ_appendix = summ % 10
            #print(f'summ_appendix {summ_appendix}')
            result.append(summ_appendix)
    if buffer > 0:
        result.append(buffer)

    return result[::-1]






def read_input() -> Tuple[List[int], int]:
    n = int(input())
    number_list = list(map(int, input().strip().split()))
    k = int(input())
    return number_list, k

number_list, k = read_input()
print(" ".join(map(str, get_sum(number_list, k))))
