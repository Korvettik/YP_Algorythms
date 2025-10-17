def is_correct_bracket_seq(instance):
    """функция принимает скобочную последовательность"""
    step_dict = dict()
    for item in instance:
        if item in ('{', '(', '['):
            if item in step_dict.keys():
                step_dict[item] += 1
            else:
                step_dict[item] = 1



    # факт наличия пары
    pairs_trigger = {'{}' : False,
                     '()' : False,
                     '[]' : False,
                     }

    if '{' in step_dict.keys():
        if '}' in step_dict.keys():
            pairs_trigger['{}'] = True

    if '(' in step_dict.keys():
        if ')' in step_dict.keys():
            pairs_trigger['()'] = True

    if '[' in step_dict.keys():
        if ']' in step_dict.keys():
            pairs_trigger['[]'] = True


    for k, v in pairs_trigger.items():
        if v is True:



    return all([
        step_dict['{'] == step_dict['}'],
        step_dict['('] == step_dict[')'],
        step_dict['['] == step_dict[']'],
                ])











instance = input().strip()
print(f'instance {instance}')
res = is_correct_bracket_seq(instance)
print(res)