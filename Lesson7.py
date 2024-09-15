# Задание 1. Новые списки
# Даны три списка. Напишите код, который создает три новых списка.
"""
from functools import reduce

floats = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]

names = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]

numbers = [22, 33, 10, 6894, 11, 2, 1]

map_result = list(map(lambda x: round(x ** 3, 3), floats))

filter_result = list(filter(lambda name: len(name) >= 5, names))

reduce_result = reduce(lambda num1, num2: num1 * num2, numbers)

print(map_result)
print(filter_result)
print(reduce_result)
"""

# Задание 2. Zip
# Даны список букв (letters) и список цифр (numbers). Каждый список состоит из 
# N элементов. Создайте кортежи из пар элементов списков и запишите их в список
# results. Не используйте функцию zip. Решите задачу в одну строку (не считая
# print(results)).
"""
from typing import List, Tuple

strings = ['a', 'b', 'c', 'd', 'e']
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

results: List[Tuple[str, int]] = list(map(lambda x, y: (x, y), strings, numbers))

print(results)
"""
# Задание 3. Палиндром
# Используя модуль collections, реализуйте функцию can_be_poly, которая
# принимает на вход строку и проверяет, можно ли получить из неё палиндром.
"""
from collections import Counter

def can_be_poly(val: str) -> bool:
    char_counts = Counter(val)
    odd_count = len(list(filter(lambda x: x % 2, char_counts.values())))
    return odd_count < 2

print(can_be_poly('eerru'))
print(can_be_poly('abbcba'))
print(can_be_poly('abbbc'))
"""
# Задание 4. Уникальный шифр
# Напишите функцию, которая принимает строку и возвращает количество
# уникальных символов в строке. Используйте для выполнения задачи
# lambda-функции и map и/или filter.
# Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного
# регистра должны считаться одинаковыми.

def count_unique_characters(string):
    lower_string = string.lower()
    unique_chars = list(filter(lambda c: lower_string.count(c.lower()) == 1, lower_string))
    
    print(unique_chars)
    
    return len(unique_chars)

message = "Today is a  beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)

print("Количество уникальных символов в строке:", unique_count)

