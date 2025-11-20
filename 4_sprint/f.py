a = int(input().strip())  # основание, по которому считается хеш.
m = int(input().strip())  #  модуль
string = input().strip()  # строка
t = int(input().strip())  # количество ввода пар индексов для подстрок

n = len(string)

# заранее вычисляем все степени a^i mod m для i от 0 до длины строки.
powers = [1] * (n + 1)  # список степеней
for i in range(1, n + 1):
    powers[i] = (powers[i - 1] * a) % m

# заранее вычисляем хеши для всех префиксов строки
prefix_hashes = [0] * (n + 1)  # список
for i in range(1, n + 1):
    prefix_hashes[i] = (prefix_hashes[i - 1] * a + ord(string[i - 1])) % m

# Обработка запросов
for _ in range(t):
    l, r = map(int, input().split())
    # Вычисляем хеш подстроки s[l-1:r]
    # Используем формулу: h = (prefix[r] - prefix[l-1] * a^(r-l+1)) mod m
    hash_value = (prefix_hashes[r] - prefix_hashes[l - 1] * powers[r - l + 1]) % m
    print(hash_value)