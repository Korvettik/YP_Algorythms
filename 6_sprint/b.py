n, m = tuple(map(int, input().strip().split()))  # n - число вершин, m - число ребер
rows = list()
for i in range(m):
    rows.append(tuple(map(int, input().strip().split())))  # ребро в виде пары вершин (u, v)    U идет в V
# print(rows)  # [(1, 3), (2, 3), (5, 2)]

# Выведите матрицу смежности n на n. На пересечении i-й строки и j-го столбца стоит единица,
# если есть ребро, ведущее из i в j.

# result_matrix = [[0]*n]*n  # [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
result_matrix = [[0 for _ in range(n)] for _ in range(n)]
#print(result_matrix)

for row in rows:
    #print(row)
    #print(f'строка {row[0]-1}')
    #print(f'столбец {row[1]-1}')
    result_matrix[row[0]-1][row[1]-1] = 1
    #print(result_matrix)

#print(result_matrix)
for row in result_matrix:
    print(*row, sep=' ')
