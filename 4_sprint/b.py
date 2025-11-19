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

from collections import defaultdict, Counter


n = int(input().strip())  # количество раундов
all_rounds_result = input().strip().split(' ')
# print(all_rounds_result)


# left_index = 0
# right_index = len(all_rounds_result)
# while left_index != right_index:
#     together_dict = Counter(all_rounds_result[left_index:right_index])
#     print(f'together_dict {together_dict}')
#     if together_dict['0'] == together_dict['1']:
#         print(len(all_rounds_result[left_index:right_index]))
#         break
#     else:
#         left_index += 1
#         right_index -= 1

counter = 0
rounds = list()
round_count_dict = defaultdict(int)
for item in all_rounds_result:
    round_count_dict[item] += 1
    counter += 1
    if round_count_dict[0] == round_count_dict[1]:
        rounds.append(counter)
    if counter > 1 and any([round_count_dict[0] == 0, round_count_dict[1] == 0]):
        counter = 1
print(max(rounds))



