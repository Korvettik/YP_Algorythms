n = int(input().strip())  # количество дней
prices_list = list(map(int, input().strip().split()))  # цены на акции
# print(n, prices)
# Выведите число, равное максимально возможной прибыли за эти дни.


total_profit = 0  # итоговый доход

if n == 0:
    print(0)
else:
    for i in range(1, n):
        if prices_list[i] > prices_list[i - 1]:
            total_profit += prices_list[i] - prices_list[i - 1]
    print(total_profit)

