default_string = input().strip()
n = int(input())

new_strings = {}
for _ in range(n):
    parts = input().strip().split()
    t = parts[0]
    k = int(parts[1])
    new_strings[k] = t

# вставок нет - просто выводим исходную строку
if not new_strings:
    print(default_string)
else:
    result_parts = []
    prev_pos = 0

    # сортируем позиции для вставки
    sorted_positions = sorted(new_strings.keys())

    for pos in sorted_positions:
        # добавляем часть оригинальной строки до позиции вставки
        if prev_pos < pos:
            result_parts.append(default_string[prev_pos:pos])

        # добавляем вставляемую строку
        result_parts.append(new_strings[pos])
        prev_pos = pos

    #остаток строки после последней вставки
    if prev_pos < len(default_string):
        result_parts.append(default_string[prev_pos:])

    # все собираем
    result = ''.join(result_parts)
    print(result)


