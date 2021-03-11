# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех слов, взятых из трёх списков
# (по одному слову из каждого списка):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
#         Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)? Сможете ли вы сделать аргументы именованными?

from random import choice

# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# jokes_list = []


# def get_one_joke():
#     """Функция возвращает одну шутку строкой"""
#     random_word_1 = choice(nouns)
#     random_word_2 = choice(adverbs)
#     random_word_3 = choice(adjectives)
#     return f'{random_word_1} {random_word_2} {random_word_3}'


def get_jokes(n, flag=False):
    """Ф-ция возвращает список шуток"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes_list = []

    if flag:
        n = min(n, len(nouns), len(adverbs), len(adjectives))


    for i in range(n):
        random_word_1 = choice(nouns)
        random_word_2 = choice(adverbs)
        random_word_3 = choice(adjectives)
        one_joke = f'{random_word_1} {random_word_2} {random_word_3}'
        jokes_list.append(one_joke)

        if flag:
            nouns.remove(random_word_1)
            adverbs.remove(random_word_2)
            adjectives.remove(random_word_3)

    return jokes_list


print(get_jokes(7, True))
