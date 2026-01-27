default_string = input().strip()
n = int(input())
new_strings = dict()
for i in range(n):
    new_string, position = input().strip().split(' ')
    new_strings[int(position)] = new_string

# print(new_strings)

total_string = ''
for i in range(len(default_string)):
    if i in new_strings.keys():  # если есть такое указание
        total_string += new_strings[i]  # вставляем слово
        total_string += default_string[i]  # родную букву
    else:
        total_string += default_string[i]

if len(default_string) in new_strings.keys():
    total_string += new_strings[len(default_string)]  # вставляем слово
    # print(total_string)

print(total_string)


