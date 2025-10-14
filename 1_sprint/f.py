def is_palindrome(line: str) -> bool:
    # Здесь реализация вашего решения
    line_list = []
    for letter in line:
        #print(f'буква {letter}')
        if letter.isalpha() or letter.isdigit():
            l_letter = letter.lower()
            line_list.append(l_letter)
            #print(line_list)
    if line_list == line_list[::-1]:
        return True
    else:
        return False

print(is_palindrome(input().strip()))
