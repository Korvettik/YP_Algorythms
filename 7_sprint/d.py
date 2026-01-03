n = int(input())
MOD = 10 ** 9 + 7  # модуль

if n <= 1:
    print(1)
else:
    prev, curr = 1, 1  # F0 и F1
    for _ in range(2, n + 1):
        prev, curr = curr, (prev + curr) % MOD
    print(curr)