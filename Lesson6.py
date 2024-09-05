# Повторение списков. Практические задания.
# Задача 1. Гласные буквы
# Функция анализатора текста - создание списка гласных букв и подсчет их количества.
"""
text = input('Введите текст: ')
vowels = [i for i in text if i in 'яауоыизюёе']
print('Список гласных букв:', vowels)
print('Длина списка:', len(vowels))
"""
# Задача 2. Случайные соревнования
"""
import random

first_team = [round(random.uniform(5,10), 2) for _ in range(20)]
second_team = [round(random.uniform(5,10), 2) for _ in range(20)]

winners = [
    first_team[i_player] if first_team[i_player] > second_team[i_player]
    else second_team[i_player]
    for i_player in range(20)
]

print('Первая команда:', first_team)
print('Вторая команда:', second_team)
print('Победители тура:', winners)
"""
# Задача 3. Двумерный список
"""
my_list = [[j_num for j_num in range(i_list, 13, 4)] for i_list in range(1, 5)]
print(my_list)

# Второй вариант решения
second_answer = [[value, value + 4, value + 8] for value in range(1, 5)]
print(second_answer)
"""
# задача 4. Список списков
"""
nice_list = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[10, 11, 12], [13, 14, 15], [16, 17, 18]]]
output = [digit
          for each_list in nice_list
          for each_list_2 in each_list
          for digit in each_list_2]
print(output)
"""
# Задача 5. Шифр Цезаря
"""
alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def caesar_cipher(string, user_shift):
    char_list = [(alphabet[(alphabet.index(sym) + user_shift) % len(alphabet)] if sym in alphabet else sym) for sym in string]
    new_str = ''.join(char_list)
    return new_str

input_str = input('Введите сообщение: ')
shift = int(input('Введите сдвиг: '))

output_str = caesar_cipher(input_str, shift)
print('Зашифрованное сообзение:', output_str)
"""