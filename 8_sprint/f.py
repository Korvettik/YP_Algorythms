from collections import defaultdict

n = int(input().strip())
words_dict = defaultdict(int)

for i in range(n):
    new_word = input().strip()
    words_dict[new_word] += 1

# print(words_dict)
word_list = list(words_dict.items())
sorted_list_desc = sorted(word_list, key=lambda x: (-x[1], x[0]), reverse=False)
print(sorted_list_desc[0][0])
