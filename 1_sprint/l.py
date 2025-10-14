from typing import Tuple

def get_excessive_letter(shorter: str, longer: str) -> str:
    # Здесь реализация вашего решения
    shorter_dict = dict()
    for letter in shorter:
        if letter not in shorter_dict.keys():
            shorter_dict[letter] = 1
        else:
            shorter_dict[letter] += 1

    longer_dict = dict()
    for letter in longer:
        if letter not in longer_dict.keys():
            longer_dict[letter] = 1
        else:
            longer_dict[letter] += 1

    #print(f'shorter_dict {shorter_dict}')
    #print(f'longer_dict {longer_dict}')

    for letter in shorter:
        #print(letter)
        if shorter_dict[letter] < longer_dict[letter]:
            return letter

    set_key = set(longer_dict.keys()) - (set(shorter_dict.keys()))
    #print(f'set_key {set_key}')
    for letter in set_key:
        return letter




def read_input() -> Tuple[str, str]:
    shorter = input().strip()
    longer = input().strip()
    return shorter, longer

shorter, longer = read_input()
print(get_excessive_letter(shorter, longer))
