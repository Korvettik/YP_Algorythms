def check_parity(a: int, b: int, c: int) -> bool:
    # Здесь реализация вашего решения

    chet = ('0', '2', '4', '6', '8')
    a_stat = False
    b_stat = False
    c_stat = False

    if str(a)[-1] in chet:
        a_stat = True
    if str(b)[-1] in chet:
        b_stat = True
    if str(c)[-1] in chet:
        c_stat = True

    if a_stat == b_stat == c_stat:
        return True
    else:
        return False


def print_result(result: bool) -> None:
    if result:
        print("WIN")
    else:
        print("FAIL")

a, b, c = map(int, input().strip().split())
print_result(check_parity(a, b, c))
