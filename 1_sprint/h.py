from typing import Tuple

def get_sum(first_number: str, second_number: str) -> str:
    # Здесь реализация вашего решения

    if len(first_number) >= len(second_number):
        biggest = first_number
        smallest = second_number

    else:
        biggest = second_number
        smallest = first_number

    biggest = biggest[::-1]
    smallest = smallest[::-1]

    for i in range(len(biggest)-len(smallest)):
        smallest += '0'

    buffer = '0'
    res_summ = ''

    for i in range(len(biggest)):

        if biggest[i] == '0' and smallest[i] == '0' and buffer == '0':
            res_summ += '0'

        elif biggest[i] == '0' and smallest[i] == '0' and buffer == '1':
            res_summ += '1'
            buffer = '0'



        elif biggest[i] == '0' and smallest[i] == '1' and buffer == '0':
            res_summ += '1'
        elif biggest[i] == '1' and smallest[i] == '0' and buffer == '0':
            res_summ += '1'

        elif biggest[i] == '0' and smallest[i] == '1' and buffer == '1':
            res_summ += '0'
        elif biggest[i] == '1' and smallest[i] == '0' and buffer == '1':
            res_summ += '0'



        elif biggest[i] == '1' and smallest[i] == '1' and buffer == '0':
            res_summ += '0'
            buffer = '1'

        elif biggest[i] == '1' and smallest[i] == '1' and buffer == '1':
            res_summ += '1'
            buffer = '1'

    if buffer == '1':
        res_summ += '1'

    return res_summ[::-1]



def read_input() -> Tuple[str, str]:
    first_number = input().strip()
    second_number = input().strip()
    return first_number, second_number

first_number, second_number = read_input()
print(get_sum(first_number, second_number))
