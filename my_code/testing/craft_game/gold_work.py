from main import gold


def gold_worker():
    gold += 100
    print('\nЗолото:', gold,
          '     Дерево:', wood,
          '     Люди:', people_1, '/', people_2,
          '     Свободные люди: ', free_people)
