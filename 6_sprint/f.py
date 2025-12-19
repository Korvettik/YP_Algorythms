n, m = tuple(map(int, input().strip().split()))  # количество вершин и ребер

# cтроим список смежности по ребрам
graph = [[] for _ in range(n)]
for i in range(m):
    u, v = tuple(map(int, input().strip().split()))
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

s, t = tuple(map(int, input().strip().split()))   # стартовая вершина и конечная

