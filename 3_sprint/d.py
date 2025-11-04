from collections import deque


def optimal_logic(n, children_factor, m, cooks_sizes):
    res_count = 0
    #print(n, children_factor, m, cooks_sizes)

    children_factor.sort()
    cooks_sizes.sort()
    cooks_sizes_deque = deque(cooks_sizes)
    #print(children_factor, cooks_sizes)

    for child_factor in children_factor:
        #  если дек не пуст
        while cooks_sizes_deque:
            cook_size = cooks_sizes_deque.popleft()
            if child_factor <= cook_size:
                res_count += 1
                break



    return res_count








n = int(input())  # количество детей
children_factor = list(map(int, input().strip().split(' ')))  # фактор жадности каждого

m = int(input())  # количество печенек
cooks_sizes = list(map(int, input().strip().split(' ')))  # размеры печенек

# Нужно выяснить, сколько ребят останутся довольными в лучшем случае,
# когда они действуют оптимально.

res_count = optimal_logic(n, children_factor, m, cooks_sizes)
print(res_count)