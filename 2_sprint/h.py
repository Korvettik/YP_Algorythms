def is_correct_bracket_seq(instance):
    """функция принимает скобочную последовательность"""
    # базово, чтобы ключи были и пары нужные
    step_dict = {'{': 1, '}': 1,
                 '(': 1, ')': 1,
                 '[': 1, ']': 1,
                 }

    for item in instance:
        step_dict[item] += 1



    return all([
        step_dict['{'] == step_dict['}'],
        step_dict['('] == step_dict[')'],
        step_dict['['] == step_dict[']'],
                ])




instance = input().strip()
res = is_correct_bracket_seq(instance)
print(res)