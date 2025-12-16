n, m = tuple(map(int, input().strip().split()))  # n - число вершин, m - число ребер
rows = list()
for i in range(m):
    rows.append(tuple(map(int, input().strip().split())))  # ребро в виде пары вершин (u, v)    U идет в V
# print(rows)  # [(1, 3), (2, 3), (5, 2)]

result = [None]*n
for row in rows:
    if result[row[0]-1] is None:
        result[row[0]-1] = [1, row[1]]
    else:
        result[row[0]-1][0] += 1
        result[row[0]-1].append(row[1])

for item in result:
    if item is None:
        print(0)
    else:
        print(*item, sep=' ')
