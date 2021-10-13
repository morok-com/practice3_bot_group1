DATABASE = {
    'Сергей': 'Омск',
    'Соня': 'Москва',
    'Миша': 'Москва',
    'Дима': 'Челябинск',
    'Алина': 'Красноярск',
    'Егор': 'Пермь',
    'Коля': 'Красноярск'
}


def format_count_friends(count_friends):
    if count_friends == 1:
        return '1 друг'
    elif 2 <= count_friends <= 4:
        return f'{count_friends} друга'
    else:
        return f'{count_friends} друзей'


def process_anfisa(query):
    if query == 'сколько у меня друзей?':
        count_string = format_count_friends(len(DATABASE))
        return f'У тебя {count_string}'
    elif query == 'кто все мои друзья?':
        friends_string = ', '.join(DATABASE.keys())
        return f'Твои друзья: {friends_string}'
    elif query == 'где все мои друзья?':
        unique_cities = set(DATABASE.values())
        cities_string = ', '.join(unique_cities)
        return f'Твои друзья в городах: {cities_string}'
    else:
        return '<неизвестный запрос>'


def runner():
    queries = [
        'Анфиса, сколько у меня друзей?',
        'Анфиса, кто все мои друзья?',
        'Анфиса, где все мои друзья?',
        'Анфиса, кто виноват?',
        'Коля, ты где?',
        'Соня, что делать?',
        'Антон, ты где?'
    ]
    for query in queries:
        print(query, '-', process_query(query))


def process_query(query):
    query_split = query.split(', ')
    if query_split[0] == 'Анфиса':
        return process_anfisa(query_split[1])
    else:
        return process_friend(query_split[0], query_split[1])


def process_friend(name, query):
    if name in DATABASE:
        if query == 'ты где?':
            return f'{name} в городе {DATABASE[name]}'
        else:
            return '<неизвестный запрос>'
    else:
        return f'У тебя нет друга по имени {name}'


runner()

# А. Напишите функцию process_friend(name, query), принимающую имя друга name и запрос query.
# Если друга с указанным именем 'Н' нет в списке, то функция должна вернуть сообщение об ошибке
# У тебя нет друга по имени Н.
# Если запрос — «ты где?», то функция должна вернуть сообщения 'Н в городе Г',
# где Г определяется по данным словаря DATABASE.
# Если запрос не «ты где?», а какой-то другой, то функция должна вернуть сообщение об ошибке <неизвестный запрос>.
# Б. Допишите функцию process_query(). Если запрос начинается не с «Анфиса», а с другого имени,
# то вызовите функцию process_friend(name, query), передав в неё имя друга и тело запроса.
# И верните результат выполнения этой функции.
# В. Добавьте в список queries новые запросы вида:
# Коля, ты где?
# Соня, что делать?
# Антон, ты где?
# Подсказка
# Первые три строки функции process_friend() могут выглядеть вот так:
# if name in DATABASE:
#     if query == 'ты где?':
#         city = DATABASE[name]