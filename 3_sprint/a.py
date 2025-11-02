def generate_bracket_sequences(n):
    """
    Генерирует все допустимые скобочные последовательности длины 2*n.
    """
    result = []

    def backtrack(curr, left, right):
        # Базовый случай: последовательность готова
        if len(curr) == 2 * n:
            result.append(curr)
            #print(f'result {result}')
            return

        # Добавляем открывающую скобку, если есть еще доступные
        if left < n:
            #print(f'( {left} < {n}')
            backtrack(curr + '(', left + 1, right)

        # После того как мы получили "(())", функция возвращается назад (backtracking) к моменту, где можно было пойти по другому пути (СЮДА)
        # Возвращаемся к состоянию: curr = "(", left = 1, right = 0
        # Раньше мы пошли по пути if left < n (добавили вторую '(').
        # Теперь пробуем другое направление — if right < left:

        # Добавляем закрывающую скобку, если она не нарушает правил
        if right < left:
            #print(f') {right} < {left}')
            backtrack(curr + ')', left, right + 1)


    backtrack('', 0, 0)

    return result

# для n = 2

#         ""
#        /
#       "("
#      /    \
#   "(("    "()"
#    /      /
# "(()"   "()("
#  /        \
# "(())"    "()()"



n = int(input().strip())  # целое число от 0 до 10
print(*generate_bracket_sequences(n), sep='\n')
