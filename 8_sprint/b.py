def check_passport(passport_name, base_name):
    len_pass, len_base = len(passport_name), len(base_name)

    if abs(len_pass - len_base) > 1:
        return "FAIL"

    if passport_name == base_name:
        return "OK"

    # если ддины равны — возможна одна замена
    if len_pass == len_base:
        diff_count = sum(1 for i in range(len_pass) if passport_name[i] != base_name[i])
        return "OK" if diff_count == 1 else "FAIL"

    # если разница в длине всего на 1 — проверяем на удаление/вставку
    shorter, longer = (passport_name, base_name) if len_pass < len_base else (base_name, passport_name)
    i, j = 0, 0
    diff = 0
    while i < len(shorter) and j < len(longer):
        if shorter[i] != longer[j]:
            diff += 1
            if diff > 1:
                return "FAIL"
            j += 1  # пропускаем один символ в более длинной строке
        else:
            i += 1
            j += 1
    return "OK"

if __name__ == "__main__":
    passport_name = input().strip()
    base_name = input().strip()
    print(check_passport(passport_name, base_name))