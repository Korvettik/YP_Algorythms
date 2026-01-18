m = int(input().strip())  #  сумма, которую нужно набрать
n = int(input().strip()) # количество монет в банкомате
nominals = map(int, input().strip().split())  # достоинства купюр


# список, где индексы - число способов набрать нужную сумму, а значения - нужная сумма
dp = [0] * (m + 1)

# один способ набрать сумму 0 (не брать ничего)
dp[0] = 1

for nominal in nominals:
    for s in range(nominal, m + 1):
        dp[s] += dp[s - nominal]

print(dp[m])