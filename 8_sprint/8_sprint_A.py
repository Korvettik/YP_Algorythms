#


# -- ПРИНЦИП РАБОТЫ ---
"""
В соответствии с условием задачи, формат входных строк записывается и интерпретируется так
abc ---- просто строчные буквы
2[ab] ----  abab
3[a]2[r2[t]] ---- aaa + rttrtt ----- aaarttrtt
2[a2[b]] ----- abbabb

Чтобы сэкономить память и время, нужно распаковывать полученные шифры строк налету и искатьмежду ними общий префикс.



"""



# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --
"""

"""



# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --
"""
Временная сложность - 
Пространственная сложность - 
"""

def unpack(s):
    stack = []  # каждый элемент: (prev_string, repeat_count)
    current_str = ""
    i = 0
    while i < len(s):
        if s[i].isdigit():
            num = 0
            while i < len(s) and s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            # s[i] == '['
            stack.append((current_str, num))
            current_str = ""
            i += 1
        elif s[i] == ']':
            prev_str, repeat = stack.pop()
            current_str = prev_str + current_str * repeat
            i += 1
        else:  # буква
            current_str += s[i]
            i += 1
    return current_str



if __name__ == "__main__":
    n = int(input())  # число строк
    strings = [input().strip() for _ in range(n)]

    unpacked = [unpack(s) for s in strings]

    # Поиск наибольшего общего префикса
    if not unpacked:
        print("")


    prefix = []
    min_len = min(len(s) for s in unpacked)

    for i in range(min_len):
        char = unpacked[0][i]
        if all(s[i] == char for s in unpacked):
            prefix.append(char)
        else:
            break

    print("".join(prefix))
