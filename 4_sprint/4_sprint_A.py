# -- ПРИНЦИП РАБОТЫ ---


# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --


# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --

def find_relevant_documents(n, letter_list, m, query_letter_list):
    """Для каждого запроса выведите на одной строке номера пяти самых релевантных документов.
    Если нашлось менее пяти документов, то выведите столько, сколько нашлось.
    Документы с релевантностью 0 выдавать не нужно."""

    relevant_list = []  # итоговый список словарей

    for query_set in query_letter_list:  # берем набор слов первого ЗАПРОСА
        query_relevant = {}  # итоговый словарь конкретного запроса  (ключ - порядковый номер документа, значение - его общая релевантность)

        for letter_dict_i in range(len(letter_list)):  # берем индекс - словарь ПЕРВОГО приложения (документа)

            for query_word in query_set:  # находим сумму всех вхождений всех слов из запроса в документе

                if query_word in letter_list[letter_dict_i].keys():
                    # суммируем для первого документа все найденные вхождения
                    if letter_dict_i + 1 not in query_relevant:
                        query_relevant[letter_dict_i + 1] = letter_list[letter_dict_i][query_word]
                    else:
                        query_relevant[letter_dict_i + 1] += letter_list[letter_dict_i][query_word]

        relevant_list.append(query_relevant)  # собираем результат в виде словаря для первого запроса


    # Вывод на экран
    #print(f'relevant_list {relevant_list}')

    # СОРТИРОВКА
    # По запросу надо вывести 5 самых релевантных документов
    # Если нашлось менее пяти документов, то выведите столько, сколько нашлось.

    # Документы с релевантностью 0 выдавать не нужно.

    # Сортировка документов на выдаче производится по убыванию релевантности.
    # Если релевантности документов совпадают —– то по возрастанию их порядковых номеров в базе (то есть во входных данных).


    for query_relevant_dict in relevant_list:
        #print(*sorted(list(query_relevant_dict.items()), key= lambda x: x[1], reverse=True)[:5])
        #print(*list(lambda x: x[0] for x in sorted(list(query_relevant_dict.items()), key= lambda x: x[1], reverse=True)[:5]), sep=' ')

        query_relevant_list = [i[0] for i in sorted(list(query_relevant_dict.items()), key= lambda x: x[1], reverse=True)[:5]]
        print(*query_relevant_list, sep=' ')











if __name__ == '__main__':

    n = int(input().strip())  # количество документов в базе
    letter_list = []  # список с подаваемыми предложениями
    for i in range(n):
        letter = input().strip().split(' ')
        letter_dict = {}
        for word in letter:
            if word in letter_dict.keys():
                letter_dict[word] += 1
            else:
                letter_dict[word] = 1
        letter_list.append(letter_dict)  # записываем предложение как словарь со словами


    m = int(input().strip())  # число запросов
    query_letter_list = []  # список с подаваемыми запросами
    for i in range(m):
        letter_set = set(input().strip().split(' '))
        query_letter_list.append(letter_set)  # записываем предложение запроса как множество со словами


    #print(f'letter_list {letter_list}')
    #print(f'query_letter_list {query_letter_list}')

    find_relevant_documents(n, letter_list, m, query_letter_list)