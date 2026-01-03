m = int(input().strip())  # максимальная грузоподъемность
n = int(input().strip())  # количество куч
heaps = []
for _ in range(n):
    c_i, m_i = map(int, input().strip().split())
    heaps.append((c_i, m_i))  # цена за кг, количество кг

# по убыванию цены за килограмм
heaps.sort(key=lambda x: x[0], reverse=True)
# print(heaps)

total_value = 0
remaining_capacity = m

for price_per_kg, kg_in_heap in heaps:
    if remaining_capacity <= 0:
        break

    # Сколько можем взять из этой кучи
    take = min(kg_in_heap, remaining_capacity)
    # print(take)
    total_value += price_per_kg * take
    remaining_capacity -= take

print(total_value)