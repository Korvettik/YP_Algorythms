#  DFS (поиск в глубину)

n, m = tuple(map(int, input().strip().split()))

# cтроим список смежности
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = tuple(map(int, input().strip().split()))
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

s = int(input().strip())
start = s - 1  # Переводим в индекс значение

# Сортируем списки смежности для каждой вершины (в порядке убывания для стека)
for i in range(n):
    graph[i].sort(reverse=True)  # Для стека нужно в обратном порядке

# DFS
visited = [False] * n
stack = [start]
result = []

while stack:
    vertex = stack.pop()

    if visited[vertex]:
        continue

    visited[vertex] = True
    result.append(vertex + 1)  # Переводим обратно в порядковый номер вершины

    # Добавляем соседей в стек
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            stack.append(neighbor)

print(*result, sep=' ')