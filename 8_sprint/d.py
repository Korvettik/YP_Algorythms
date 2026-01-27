n = int(input().strip())
max_prefix = 0
letters = []
for i in range(n):
    letters.append(input().strip())

minimum_word = min(letters)
count = 0

for i in range(len(minimum_word)):
    for letter in letters:
        if minimum_word[i] == letter[i]:
            count += 1

    if count == len(letters):
        max_prefix += 1
        count = 0
    else:
        break
print(max_prefix)
