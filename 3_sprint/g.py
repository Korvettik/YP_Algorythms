# Рита захотела отсортировать свой новый гардероб по цветам.
# Сначала должны идти вещи розового цвета, потом —– жёлтого, и в конце —– малинового.

def sortiration_func(n, colors_string):
    if n > 0:
        woodrope = list(map(int, colors_string.strip().split(' ')))

        #print(n, woodrope)
        rose = []
        yellow = []
        wildberry = []
        for weather in woodrope:
            if weather == 0:
                rose.append(0)
            elif weather == 1:
                yellow.append(1)
            elif weather == 2:
                wildberry.append(2)
        res = rose + yellow + wildberry
        print(*res, sep=' ')
    else:
        return



n = int(input().strip())  # количество предметов в гардеробе
# Розовый цвет обозначен  0,
# жёлтый —– 1,
# малиновый –— 2
colors_string = input()
sortiration_func(n, colors_string)
