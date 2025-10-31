def generate_words(command):
    """генерирует возможные комбинации по строке, предполагаю дубли"""
    print(command)

    result = []

    buttons = {
        '2': ('a', 'b', 'c'),
        '3': ('d', 'e', 'f'),
        '4': ('g', 'h', 'i'),
        '5': ('j', 'k', 'l'),
        '6': ('m', 'n', 'o'),
        '7': ('p', 'q', 'r', 's'),
        '8': ('t', 'u', 'v'),
        '9': ('w', 'x', 'y', 'z')
        }


    def backtrack(word):
        # Базовый случай
        if len(word) == len(command):  # количество букв результирующего слова равно числу символов команды
            result.append(word)
            return

        for num in command:
            for letter in buttons[num]:

            if index < len(buttons[num]):

                backtrack(word += buttons[num][index], )





    backtrack('', 0)

    return result



# На вход подается строка, состоящая из цифр 2-9 включительно.
# Длина строки не превосходит 10 символов.

command = list(input().strip())  # строка команд без повторов

print(*generate_words(command), sep=' ')
