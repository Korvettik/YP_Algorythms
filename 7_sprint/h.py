n, m = map(int, input().strip().split())  # размеры поля
matrix = []
for i in range(n):
    matrix.append(list(map(int, list(input().strip()))))
# print(matrix)

dp = [[0] * m for _ in range(n)]

# начальная клетка
dp[n-1][0] = matrix[n-1][0]

# заполняем самый левый столбец, идем только снизу вверх
for i in range(n-2, -1, -1):
    dp[i][0] = dp[i+1][0] + matrix[i][0]

# заполняем САМУЮ нижнюю строку, идем только слева направо
for j in range(1, m):
    dp[n-1][j] = dp[n-1][j-1] + matrix[n-1][j]

#  остальное
for i in range(n-2, -1, -1):
    for j in range(1, m):
        dp[i][j] = max(dp[i+1][j], dp[i][j-1]) + matrix[i][j]

# ответ будет в правом верхнем углу
print(dp[0][m-1])