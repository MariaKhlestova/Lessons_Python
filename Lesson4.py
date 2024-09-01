# Задача 1. Три списка
"""
array_1 = [1, 5, 10, 20, 40, 80, 100]
array_2 = [6, 7, 20, 80, 100]
array_3 = [3, 4, 15, 20, 30, 70, 80, 120]

# задача 1 
# без использования множеств

all_elems = array_1 + array_2 + array_3 
new_elems_1 = []
for elem in all_elems:
    if elem not in new_elems_1 and all(elem in array for array in [array_1, array_2, array_3]):
        new_elems_1.append(elem)
print("Решение без множеств: ", new_elems_1)

# с множеством

new_elems_1_set = set(array_1) & set(array_2) & set(array_3)
print("Решение с множествами: ", new_elems_1_set)

# задача 2
# без использования множеств
new_elems_2 = []
for elem in array_1:
    if elem not in array_2 and elem not in array_3:
        new_elems_2.append(elem)
print("Решение без множеств: ", new_elems_2)

# с множеством

new_elems_2_set = set(array_1) - set(array_2) - set(array_3)
print("Решение с множествами: ", new_elems_2_set)
"""

# Задача 2. Палиндром
"""
def is_poly(string):
    char_dict = dict()
    for i_sym in string:
        char_dict[i_sym] = char_dict.get(i_sym, 0) + 1
    
    odd_count = 0
    for i_value in char_dict.values():
        if i_value % 2 != 0:
            odd_count += 1
    return odd_count <= 1

my_string = input("Введите строку: ")
if is_poly(my_string):
    print("Можно сделать палиндромом")
else:
    print("Нельзя сделать палиндромом")
"""
# Задача 3. Словарь синонимов
"""
synonyms_dict = dict()
pairs_count = int(input("Введите количество пар слов: "))

for i_pair in range(pairs_count):
    first_word, second_word = input(f"{i_pair+1} пара: ").lower().split(" - ")
    synonyms_dict[first_word] = second_word
    synonyms_dict[second_word] = first_word

while True:
    word = input("Введите слово: ").lower()
    
    if word in synonyms_dict:
        print("Синоним: ", synonyms_dict[word].capitalize())
        break
    else:
        print("Такого слова в словаре нет.)")
"""
# Задача 4. Гистограмма частоты
"""
def histogram(string):
    sym_dict = dict ()
    for sym in string:
        if sym in sym_dict:
            sym_dict[sym] += 1
        else:
            sym_dict[sym] = 1
    return sym_dict

def invert_dict(d):
    inv = dict()
    
    for key in d:
        val = d[key]
        
        if val not in inv:
            inv[val] = [key]
        else:
            inv[val].append(key)
    return inv

text = input("Введите текст: ")
hist = histogram(text)

print("Оригинальный словарь частот: ")
for i_sym in sorted(hist.keys()):
    print(i_sym, ':', hist[i_sym])
    
inv_hist = invert_dict(hist)

print("\nИнвертированный словарь частот: ")

for i_sym in sorted(inv_hist.keys()):
    print(i_sym, ':', inv_hist[i_sym])
"""