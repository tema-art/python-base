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
        return None
