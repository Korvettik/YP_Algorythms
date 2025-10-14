def is_power_of_four(number: int) -> bool:
    # Здесь реализация вашего решения
    total = 4

    if number in (1, 4):
        return True

    while total < number:
        total *= 4
        if total == number:
            return True


    return False

print(is_power_of_four(int(input())))
