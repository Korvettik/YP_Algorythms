n = int(input().strip())  # количество строк лога
logs_set = set()
for _ in range(n):
    log = input().strip()
    if log not in logs_set:
        logs_set.add(log)
        print(log)
