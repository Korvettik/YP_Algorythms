def generate_bracket_sequences(n):
    """
    Генерирует все допустимые скобочные последовательности длины 2*n.

    Args:
        n: Целое число, половина длины желаемой последовательности.
    """
    result = []

    def backtrack(curr, left, right):
        # Базовый случай: последовательность готова
        if len(curr) == 2 * n:
            result.append(curr)
            return

        # Добавляем открывающую скобку, если есть еще доступные
        if left < n:
            backtrack(curr + '(', left + 1, right)

        # Добавляем закрывающую скобку, если она не нарушает правил
        if right < left:
            backtrack(curr + ')', left, right + 1)

    backtrack('', 0, 0)
    return result

# Пример использования:
print(generate_bracket_sequences(3))
# Вывод: ['((()))', '(()())', '(())()', '()(())', '()()()']



n = int(input().strip())  # целое число от 0 до 10
generate_bracket_sequences(n)