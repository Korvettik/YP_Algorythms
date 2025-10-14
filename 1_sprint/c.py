from typing import List, Tuple

def get_neighbours(matrix: List[List[int]], row: int, col: int) -> List[int]:
    # Здесь реализация вашего решения
    res = list()
    if row > 0:
        res.append(matrix[row-1][col])  # верх

    if row < len(matrix)-1:
        res.append(matrix[row+1][col])  # низ

    if col > 0:
        res.append(matrix[row][col-1])  # левый край

    if col < len(matrix[row])-1:
        res.append(matrix[row][col+1])  # правый край

    return sorted(res)






def read_input() -> Tuple[List[List[int]], int, int]:
    n = int(input())
    m = int(input())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, input().strip().split())))
    row = int(input())
    col = int(input())
    return matrix, row, col

matrix, row, col = read_input()
print(" ".join(map(str, get_neighbours(matrix, row, col))))
