from collections import deque

n, m = map(int, input().strip().split())

# cтроим список смежности, индексы от нуля
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = map(int, input().strip().split())
    graph[u - 1].append(v - 1)
    graph[v - 1].append(u - 1)

visited = [False] * n
total_groups = []

# обходим все вершины
for i in range(n):
    if not visited[i]:
        # начинаем новую компоненту связности
        group = []
        queue = deque([i])
        visited[i] = True

        # BFS обход
        while queue:
            vertex = queue.popleft()
            group.append(vertex + 1)  # преобразуем обратно в порядковые номера вершин

            # добавляем всех непосещенных соседей
            for neighbor in graph[vertex]:
                if not visited[neighbor]:
                    visited[neighbor] = True
                    queue.append(neighbor)

        # сортировка в самой группе
        group.sort()
        total_groups.append(group)

# сортируем группы по номеру первой вершины
total_groups.sort(key=lambda x: x[0])

# выводим все
print(len(total_groups))
for group in total_groups:
    print(' '.join(map(str, group)))