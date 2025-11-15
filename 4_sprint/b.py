from collections import Counter


n = int(input().strip())  # количество раундов
all_rounds_result = input().strip().split(' ')
# print(all_rounds_result)

left_index = 0
right_index = len(all_rounds_result)
while left_index != right_index:
    together_dict = Counter(all_rounds_result[left_index:right_index])
    print(f'together_dict {together_dict}')
    if together_dict['0'] == together_dict['1']:
        print(len(all_rounds_result[left_index:right_index]))
        break
    else:
        left_index += 1
        right_index -= 1

