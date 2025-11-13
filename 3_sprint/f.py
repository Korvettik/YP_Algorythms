from collections import deque

def longest_triangle_perimeter(n, lines):
    #print(n, lines)

    lines.sort(reverse=True)
    #print(lines)
    lines_deque = deque(lines)
    while lines_deque:
        bigest_line = lines_deque.popleft()
        if len(lines_deque) >= 2:
            second_line = lines_deque.popleft()
            third_line = lines_deque.popleft()

            if bigest_line < second_line + third_line:
                return bigest_line + second_line + third_line
            else:
                lines_deque.appendleft(third_line)
                lines_deque.appendleft(second_line)
    return 0






n = int(input().strip())  # количество отрезков
lines = list(map(int, input().strip().split(' ')))  # список длин отрезков

# Нужно вывести одно число —– наибольший периметр треугольника.
# Гарантируется, что тройка чисел, которая может образовать треугольник, всегда есть.

res = longest_triangle_perimeter(n, lines)
print(res)