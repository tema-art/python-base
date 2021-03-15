# Задание 2. Курс Валюты
# Написать функцию get_currency_rate(), принимающую в качестве аргумента код валюты
# (например, USD, EUR, GBP, ...) в виде строки и возвращающую курс этой валюты по отношению к рублю.
# Код валюты может быть в произвольном регистре.
# Функция должна возвращать результат числового типа, например float.
# Если в качестве аргумента передали код валюты, которого нет в ответе, вернуть None.
# Используйте библиотеку requests, чтобы забрать актуальные данные из ЦБ РФ по адресу
# http://www.cbr.ru/scripts/XML_daily.asp.
#
# Выведите на экран курсы для доллара и евро, используя написанную функцию.
#
# Рекомендация: выполнить предварительно запрос к этой странице в обычном браузере, посмотреть содержимое ответа.
# <Valute ID="R01035">
# <NumCode>826</NumCode>
# <CharCode>GBP</CharCode>
# <Nominal>1</Nominal>
# <Name>Фунт стерлингов Соединенного королевства</Name>
# <Value>102,5099</Value>
# </Valute>
#
# <Valute ID="R01235">
# <NumCode>840</NumCode>
# <CharCode>USD</CharCode>
# <Nominal>1</Nominal>
# <Name>Доллар США</Name>
# <Value>73,4996</Value>
# </Valute>
#
# <Valute ID="R01239">
# <NumCode>978</NumCode>
# <CharCode>EUR</CharCode>
# <Nominal>1</Nominal>
# <Name>Евро</Name>
# <Value>87,7585</Value>
# </Valute>

# print(nums.index('73'))
# print(nums[57])
# print(nums.index('4996'))
# print(nums[58])
# print(nums.index('87'))
# print(nums[62])
# print(nums.index('7585'))
# print(nums[63])
import re
import requests
import datetime


# print(help(requests)
import re
import requests

def get_currency_rate(currency):

    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')

    nums = re.findall(r'\d*\.\d+|\d+', r.text)
    num_list1 = []
    num_list2 = []
    num_list1.append(nums[57])
    num_list1.append(nums[58])
    num_list2.append(nums[62])
    num_list2.append(nums[63])
    dollar = float('.'.join(num_list1))
    euro = float('.'.join(num_list2))
    if currency.upper() == 'USD':
        print("USD", dollar)
    elif currency.upper() == 'EUR':
        print("EUR", euro)
    else:
        print(None)


get_currency_rate('usd')
get_currency_rate('EUR')
get_currency_rate('ffff')




#     print(usd, eur)
#    print(type(usd), type(eur))
# if USD == True:
#     print("Курс доллара: ", usd)
# elif EUR in currency:
#     print("Курс евро: ", eur)


# return usd, eur
# def get_currency_rate(currency):
#     r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
#     print
