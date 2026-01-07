x = int(input().strip())  # требуемая сумма
k = int(input().strip())  # количество номиналов
nominals = list(set(map(int, input().strip().split())))  # уникальные возможные номиналы
nominals.sort(reverse=True)


# dp[i] - минимальное количество купюр для набора суммы i
INF = 10**9
dp = [INF] * (x + 1)
dp[0] = 0  # для суммы 0 нужно 0 купюр

# заполняем
for i in range(1, x + 1):
    for nominal in nominals:
        if i - nominal >= 0:
            dp[i] = min(dp[i], dp[i - nominal] + 1)

# если dp[x] осталось INF, значит сумму набрать невозможно
result = dp[x] if dp[x] != INF else -1
print(result)
