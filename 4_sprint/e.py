# import random
# import string
#
#
# base = 1000
# tablesize = 123_987_123
#
#
# def polynomial_hash(str, p, m):
#     power_of_p = 1
#     hash_val = 0
#
#     for char in str:
#         hash_val = ((hash_val + ord(char) * power_of_p) % m)
#         power_of_p = (power_of_p * p) % m
#
#     return int(hash_val)
#
# letters = string.ascii_lowercase
# str = ''.join(random.choice(letters) for i in range(10))
# hash = polynomial_hash(str[::-1], base, tablesize)
# map = {}
#
# while True:
#     str = ''.join(random.choice(letters) for i in range(20))
#     hash = polynomial_hash(str[::-1], base, tablesize)
#     if not map.get(hash):
#         map[hash] = str
#     else:
#         print(f"{str} - {hash}")
#         break




def polynomial_hash(s, p=1000, m=123987123):
    """Полиномиальный хеш с заданными параметрами"""
    hash_value = 0
    n = len(s)

    for i, char in enumerate(s):
        char_code = ord(char)
        power = pow(p, n - 1 - i, m)
        hash_value = (hash_value + char_code * power) % m

    return hash_value

def find_collision():
    """
    Находит коллизию для p=1000, m=123987123
    """
    import random
    import string

    hashes = {}
    attempts = 0
    max_attempts = 1000000

    # Генерируем случайные строки
    while attempts < max_attempts:
        # Случайная длина от 3 до 10 символов
        length = random.randint(3, 10)
        random_str = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

        h = polynomial_hash(random_str, 1000, 123987123)

        if h in hashes:
            existing_str = hashes[h]
            if existing_str != random_str:
                print(f"Найдена коллизия на попытке {attempts}:")
                print(f"'{existing_str}' -> {h}")
                print(f"'{random_str}' -> {h}")
                return (existing_str, random_str)

        hashes[h] = random_str
        attempts += 1

        if attempts % 100000 == 0:
            print(f"Попытка {attempts}...")

    print("Коллизия не найдена за максимальное число попыток")
    return None

find_collision()