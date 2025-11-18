from collections import defaultdict

# Для каждой пары символов (s[i], t[i]) проверяем двустороннее соответствие
# Если символ s уже встречался, он должен соответствовать тому же символу t
# Если символ t уже встречался, он должен соответствовать тому же символу s

def logic(s, t):

    if len(s) != len(t):
        return False

    else:
        s_to_t = dict()
        t_to_s = dict()

        for char_s, char_t in zip(s, t):
            # Проверяем соответствие букв s -> t
            if char_s in s_to_t:
                if s_to_t[char_s] != char_t:
                    return False
            else:
                s_to_t[char_s] = char_t

            # Проверяем соответствие t -> s
            if char_t in t_to_s:
                if t_to_s[char_t] != char_s:
                    return False
            else:
                t_to_s[char_t] = char_s

        return True


s = input().strip()  # первая строка
t = input().strip()  # вторая строка

if logic(s, t):
    print('YES')
else:
    print('NO')