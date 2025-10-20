

def read_input():
    """получаем данные задачи из стандартного ввода"""
    n, k = list(map(int, input().strip().split()))  # целые числа
    return n, k






def iteration_logic(n, k):
    """логика рекурсивного прохождения по элементам"""

    MOD = 10**k
    a, b = 0, 1
    for _ in range(n):
        a, b = b % MOD, (a + b) % MOD

    return b


if __name__ == '__main__':
    """функция точки входа общей логики"""

    n, k = read_input()

    result_commit_count = iteration_logic(n, k)
    print(f'{result_commit_count}')



