# полиномиальный хэш


a = int(input().strip())  # основание, по которому считается хеш.
m = int(input().strip())  #  модуль
s = input().strip()  # строка

lenth = len(s)
hash_summ = 0
power = 1

for letter in s[::-1]:
    hash_summ = ((hash_summ + ord(letter) * power) % m)
    power = (power * a) % m


print(hash_summ)