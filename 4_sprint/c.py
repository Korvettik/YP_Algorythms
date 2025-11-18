from collections import defaultdict
s = input().strip()  # первая строка
t = input().strip()  # вторая строка


s_len = len(s)
t_len = len(t)

s_dict = defaultdict(list)
t_dict = defaultdict(list)

if s_len == t_len:
    for i in range(s_len):
        s_dict[s[i]].append(i)
    #print(s_dict)

    for i in range(t_len):
        t_dict[t[i]].append(i)
    #print(t_dict)

    flag = True
    for indexes in s_dict.values():
        if indexes not in t_dict.values():
            print('NO')
            flag = False
            break
    if flag:
        print('YES')



else:
    print('NO')