x = int(input().strip())  # требуемая сумма
k = int(input().strip())  # количество номиналов
nominals = list(set(map(int, input().strip().split())))  # уникальные возможные номиналы
nominals.sort(reverse=True)
print(nominals)

counts = 0
remaining_summ = x

for nominal in nominals:
    if remaining_summ <= 0:
        break

    # Сколько можем взять из этой кучи
    take = min(nominal, remaining_summ)
    # print(take)
    total_value += price_per_kg * take
    remaining_capacity -= take