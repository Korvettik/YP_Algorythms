from math import floor
from typing import List
import math

def factorize(number: int) -> List[int]:
    # Здесь реализация вашего решения
    start_number = number
    stop_shag = int(math.sqrt(number))  # ищем до квадрата, дальше бесполезно
    #print(f'stop_shag {stop_shag}')

    res_list = []
    shag = 2

    while shag <= stop_shag:
        appendix = number % shag
        if appendix == 0:
            res_list.append(shag)
            #print(f'res_list {res_list}')
            number //= shag
        else:
            if shag >= 3:  # пропускаем все четные числа после 2
                shag += 2
            else:
                shag += 1

    total = 1
    for i in res_list:
        total *= i
    #print(f'total {total}')

    last_digit = int(start_number / total)
    # print(f'last_digit {last_digit}')
    if last_digit > 1:
        res_list.append(last_digit)



    return sorted(res_list)






result = factorize(int(input()))
print(" ".join(map(str, result)))
