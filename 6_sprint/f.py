# Найдите кратчайшее расстояние между парой вершин в неориентированном графе. Граф может быть несвязным.
# Выведите длину кратчайшего пути (в рёбрах) между заданной парой вершин. Если пути не существует, то выведите −1.

from collections import deque
n, m = tuple(map(int, input().strip().split()))  # количество вершин и ребер

# cтроим список смежности по ребрам
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = tuple(map(int, input().strip().split()))
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

s, t = tuple(map(int, input().strip().split()))   # стартовая вершина и конечная
s -= 1  # преобразуем в индексацию от нуля
t -= 1  # преобразуем в индексацию от нуля

# print(graph)

def bfs_shortest_path(start, end):
    # защита, если начальная и конечная вершины совпадают
    if start == end:
        return 0

    # очередь для BFS, храним (вершина, расстояние - в шагах)
    queue = deque([(start, 0)])

    # список для отметки посещенных вершин
    visited = [False] * n
    visited[start] = True

    while queue:
        vertex, dist = queue.popleft()

        # перебираем соседей текущей вершины
        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                # если достигли конечной вершины, выход
                if neighbor == end:
                    return dist + 1  # +1 для ребра от vertex к neighbor

                # продолжаем
                visited[neighbor] = True
                queue.append((neighbor, dist + 1))

    # если не нашли путь
    return -1


result = bfs_shortest_path(s, t)
print(result)