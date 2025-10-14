def to_binary(number: int) -> str:
    # Здесь реализация вашего решения
    if number == 0:
        return str(0)

    else:
        res_binary = ''
        while number > 0:
            digit = str(number % 2)
            number = number // 2
            #print(f'digit {digit}')
            #print(f'number {number}')
            res_binary += digit
        #print(f'res_binary {res_binary}')
        return res_binary[::-1]



def read_input() -> int:
    return int(input().strip())

print(to_binary(read_input()))
