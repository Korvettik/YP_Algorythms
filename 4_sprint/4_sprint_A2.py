# -- ПРИНЦИП РАБОТЫ ---
from collections import defaultdict, Counter


# -- ДОКАЗАТЕЛЬСТВА КОРРЕКТНОСТИ --


# -- ОПРЕДЕЛЕНИЕ СЛОЖНОСТИ АЛГОРИТМА --

def find_relevant_documents(n, letter_list, m, query_letter_list):
    """
    Для каждого запроса выведите на одной строке номера пяти самых релевантных документов.
    Если нашлось менее пяти документов, то выведите столько, сколько нашлось.
    Документы с релевантностью 0 выдавать не нужно.

    Подумайте над случаями, когда запросы состоят из слов,
    встречающихся в малом количестве документов.

    Что если одно слово много раз встречается в одном документе?
    """


    # Создаем один общий пустой словарь.
    # Если в словаре не будет найден какой-либо ключ, то он будет создан со значением по умолчанию  - тут dict - пустой словарь.
    # т.е. это будет словарь словарей    {'i': {0: 1}, 'love': {0: 1}, 'coffee': {0: 1, 1: 1}}
    index = defaultdict(dict)
    #print(f'index {index}')

    # проходимся по кортежам (номер предложения, список слов предложения)
    for doc_id, letter_words in enumerate(letter_list):

        # Автоподсчет количества встречаемых слов (словарь, где ключ - уникальное слово, значение - сколько раз оно встретилось в подаваемом предложении)
        letter_word_counts_dict = Counter(letter_words)
        #print(f'letter_word_counts_dict {letter_word_counts_dict}')

        # добавляем в общий словарь статистику для слова + где и сколько раз оно встречается
        for word, count in letter_word_counts_dict.items():
            index[word][doc_id] = count
            #print(index)

    # итого мы имеем что-то такое
    # index = {'i': {0: 1}, 'love': {0: 1}, 'coffee': {0: 1, 1: 1}}




    results = []  # будущий общий результат

    # берем уникальные (множество) слова ПЕРВОГО запроса
    for letter_query_set in query_letter_list:
        #print(letter_query_set)

        # Собираем все документы, содержащие хотя бы одно слово из запроса
        candidate_docs = set()
        for word in letter_query_set:
            if word in index:
                candidate_docs.update(index[word].keys())

        # Вычисляем релевантность для каждого документа-кандидата
        scores = []
        for doc_id in candidate_docs:
            relevance = 0
            for word in letter_query_set:
                if word in index and doc_id in index[word]:
                    relevance += index[word][doc_id]

            # Добавляем только документы с ненулевой релевантностью
            if relevance > 0:
                # Используем отрицательную релевантность для сортировки по убыванию,
                # и положительный doc_id для сортировки по возрастанию при равенстве релевантности
                scores.append((-relevance, doc_id))

        # Сортируем и берем топ-5
        scores.sort()
        top_docs = []
        for score, doc_id in scores[:5]:
            # Номера документов в выводе начинаются с 1
            top_docs.append(str(doc_id + 1))

        results.append(" ".join(top_docs))

    # Вывод результатов
    for result in results:
        print(result)







if __name__ == '__main__':

    n = int(input().strip())  # количество документов в базе

    letter_list = []  # список с подаваемыми предложениями
    for i in range(n):
        letter = input().strip().split(' ')
        letter_list.append(letter)  # список списков


    m = int(input().strip())  # число запросов
    query_letter_list = []  # список с подаваемыми запросами
    for i in range(m):
        letter_set = set(input().strip().split(' '))
        query_letter_list.append(letter_set)  # записываем предложение запроса как множество со словами


    #print(f'letter_list {letter_list}')
    #print(f'query_letter_list {query_letter_list}')

    find_relevant_documents(n, letter_list, m, query_letter_list)