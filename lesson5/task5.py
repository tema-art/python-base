from collections import OrderedDict

# 5. Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
# Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с
# сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
# result = [23, 1, 3, 10, 4, 11]
# Подсказка: напишите сначала решение «в лоб». Потом подумайте об оптимизации.


# num_list = [i for i in range(len(src)) if i == 1]
#
# print(num_list)

# for i in range(len(src)):
#     for j in range(len(src)):
#         if src(i) == src(j) and i != j:
#             break
#         else:
#             print(src[i])

for i in range(len(src)):  # 1-ый вариант, не понимаю почему нет 23, порядок не сохранён
    if src.count(i) == 1:
        print(i)

print(list(OrderedDict.fromkeys(src)))  # 2-ой вариант, по прядку, но имеются по одному элементу из повторяющихся
# print(set(src))

my_list = []  # 3-вариант без библиотеки, так же имеются по одному элементу из повторяющихся
for i in src:
    if i not in my_list:
        my_list.append(i)
print(my_list)

my_list2 = set()
src_unique = [i for i in src if i not in my_list2 and (my_list2.add(i) or True)]
print(src_unique)
# 4 вариант через ListComrehensions, та же проблема
