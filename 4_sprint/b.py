#  раунд отсекается, потому что условие "ничьи" относится не к отдельным играм, а к общему счету очков, набранных в определенном диапазоне раундов.

# 1: 1–0
# 2: 2–0
# 3: 2–1
# 4: 3–1
# 5: 3–2
# 6: 3–3 = ничья
# 7: 3–4
# 8: 4–4 = ничья
# 9: 5–4
# 10: 6–4

from collections import defaultdict


n = int(input().strip())  # количество раундов
all_rounds_result = list(map(int, input().strip().split()))

# Используем словарь для хранения первого вхождения каждой разницы
first_occurrence = defaultdict(int)
first_occurrence[0] = 0  # Разница 0 перед началом турнира

max_length = 0
diff = 0  # Разница между количеством 0 и 1

for i in range(1, n + 1):
    # Обновляем разницу
    if all_rounds_result[i-1] == 0:
        diff += 1
    else:
        diff -= 1

    # Если такая разница уже встречалась, значит между этими позициями ничья
    if diff in first_occurrence:
        max_length = max(max_length, i - first_occurrence[diff])
    else:
        # Запоминаем первое вхождение этой разницы
        first_occurrence[diff] = i

print(max_length)



