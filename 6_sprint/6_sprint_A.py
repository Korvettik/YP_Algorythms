# -- ПРИНЦИП РАБОТЫ ---
"""

"""

# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --
"""

"""

# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --
"""

"""


import heapq

def make_reach_net():
    # n - количество вершин
    # m - количество ребер
    n, m = tuple(map(int, input().strip().split()))
    #print(n, m)

    # строим список смежности
    graph = [[] for _ in range(n)]  # список пустых списков
    #print(graph)

    # заполняем его полученными данными
    # В каждой из следующих m строк заданы рёбра в виде троек чисел u,v,w.
    # u и v — вершины, которые соединяет это ребро.
    # w — его вес
    for _ in range(m):
        u,v,w = tuple(map(int, input().strip().split()))

        # игнорируем такие ребра, так как они бесполезны для остовного дерева
        if u == v:
            continue

        # 1) индексы вершин в списке с нуля, но подаются вершины с 1 (по условию)
        # поэтому переводим номера вершин в индексы списка (-1) и в таком виде записываем

        # 2) в индекс-вершину (являющуюся списком) добавляем в виде кортежей информацию о ребрах
        # (вес ребра, в какую вершину ведет), причем сразу добавляем и обратное ребро.
        # [[(5, 1), (6, 2)], [(5, 0), (8, 3)], [(6, 0), (3, 3)], [(8, 1), (3, 2)]]
        graph[u-1].append((w, v-1))
        graph[v-1].append((w, u-1))
    # print(graph)


    # Для графа с одной вершиной
    if n <= 1:
        print(0)
        return

    visited = [False] * n
    max_heap = []

    # Инициализируем первую вершину
    visited[0] = True
    for weight, neighbor in graph[0]:
        if not visited[neighbor]:
            heapq.heappush(max_heap, (-weight, neighbor))

    total_weight = 0
    vertices_in_mst = 1

    while max_heap and vertices_in_mst < n:
        neg_weight, vertex = heapq.heappop(max_heap)

        if visited[vertex]:
            continue

        weight = -neg_weight
        visited[vertex] = True
        total_weight += weight
        vertices_in_mst += 1

        # Добавляем только рёбра к непосещённым вершинам
        for w, neighbor in graph[vertex]:
            if not visited[neighbor]:
                heapq.heappush(max_heap, (-w, neighbor))

    # Проверка связности
    if vertices_in_mst == n:
        print(total_weight)
    else:
        print("Oops! I did it again")



if __name__ == "__main__":
    make_reach_net()