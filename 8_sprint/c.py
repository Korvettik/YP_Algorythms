s = input().strip()  # исходная строка

freq = [0] * 26   # частоты повторений букв в алфавите общем a ... z

# подсчитываем частоты встречаемости букв
for ch in s:
    freq[ord(ch) - ord('a')] += 1

# собираем левую половинку (реверсом она будет и правой)
left_part = []
for i in range(26):
    left_part.append(chr(ord('a') + i) * (freq[i] // 2))

left_str = ''.join(left_part)

# выбираем среднюю букву
mid_char = ''
for i in range(26):
    if freq[i] % 2 == 1:
        mid_char = chr(ord('a') + i)
        break

# собираем все вместе
result = left_str + mid_char + left_str[::-1]
print(result)


