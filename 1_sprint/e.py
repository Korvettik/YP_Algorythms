def get_longest_word(line: str) -> str:
    # Здесь реализация вашего решения
    longest_word = ''
    line_list = line.split()
    for word in line_list:
        if len(word) > len(longest_word):
            longest_word = word
    return longest_word




def read_input() -> str:
    _ = input()
    line = input().strip()
    return line

def print_result(result: str) -> None:
    print(result)
    print(len(result))

print_result(get_longest_word(read_input()))
