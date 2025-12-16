# BFS (поиск в ширину)

from collections import deque

n, m = tuple(map(int, input().strip().split()))

# Строим список смежности
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = tuple(map(int, input().strip().split()))
    # Преобразуем в 0-based индексы
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

s = int(input().strip())
start = s - 1  # Переводим в индекс значение

# Сортируем списки смежности для каждой вершины - в порядке возрастания
for i in range(n):
    graph[i].sort()

# BFS обход
visited = [False] * n
queue = deque()
result = []

# Начинаем со стартовой вершины
queue.append(start)
visited[start] = True

while queue:
    vertex = queue.popleft()
    result.append(vertex + 1)  #  Переводим обратно в порядковый номер вершины

    # Добавляем всех непосещенных соседей в очередь
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            visited[neighbor] = True
            queue.append(neighbor)

print(*result, sep=' ')