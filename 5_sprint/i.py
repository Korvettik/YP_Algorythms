n = int(input().strip())

# Вычисляем число Каталана как есть

def factorial(x):
    # вычисление факториала
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result

# C(n) = (2n)! / ((n+1)! * n!)
catalan = factorial(2 * n) // (factorial(n + 1) * factorial(n))
print(catalan)