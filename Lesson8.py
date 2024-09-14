# Задание 1. Сумма чисел
# Во входном файле numbers.txt записано N целых чисел, которые могут быть 
# разделены пробелами и концами строк. Напишите программу, которая выводит 
# сумму чисел во выходной файл answer.txt.
"""
import os

numbers_file = open("numbers.txt", "r", encoding="utf-8")

total_sum = 0

for line in numbers_file:
    numbers = [int(num) for num in line.split() if num]
    total_sum += sum(numbers)
    
numbers_file.close()

sum_file = open("answer.txt", "w", encoding="utf-8")

sum_file.write(str(total_sum))
sum_file.close()
"""
# Задание 2. Сумма чисел
# В файле zen.txt хранится так называемый Дзен Пайтона — текст философии 
# программирования на языке Python. 
# Напишите программу, которая выводит на экран все строки этого файла в 
# обратном порядке.
"""
philosophical_text = open("zen.txt", "r")
lines = philosophical_text.readlines()
philosophical_text.close()

for line in reversed(lines):
    print(line.strip())
"""

# Задание 3. Турнир
# В файле first_tour.txt записано число K и данные об участниках турнира по 
# настольной игре «Орлеан»: фамилии, имена и количество баллов, набранных в 
# первом туре. Во второй тур проходят участники, которые набрали более K баллов в первом туре.
# Напишите программу, которая выводит в файл second_tour.txt данные всех участников, прошедших во второй тур, с нумерацией.
"""
with open("first_tour.txt", "r") as file:
    lines = file.readlines()
    k = int(lines[0])
    participants = {}
    filter_player = {}
    count = 1

for line in lines[1:]:
    data = line.strip().split()
    name = f"{data[1][0]}. {data[0]}"
    score = int(data[-1])
    participants[name] = score
    
for player, score in participants.items():
    if score > k:
        filter_player[player] = score
sorted_filter_player = dict(sorted(filter_player.items(), key=lambda x: x[1], reverse=True))

with open("second_tour.txt", "w") as file:
    file.write(f"{len(sorted_filter_player)}\n")
    
    for player, score in sorted_filter_player.items():
        file.write(f"{count}) {player} {score}\n")
        count += 1
"""
# задание 4. Частотный анализ
# Есть файл text.txt, который содержит текст. Напишите программу, которая 
# выполняет частотный анализ, определяя долю каждой буквы английского 
# алфавита в общем количестве английских букв в тексте, и выводит результат в файл analysis.txt. 
# Символы, не являющиеся буквами английского алфавита, учитывать не нужно.
"""
english_alphabet = 'abcdefghijklmnoprstuvwxyz'
total_letters = 0

with open("text.txt", "r") as file:
    text = file.read().lower()

letter_count = {letter: 0 for letter in english_alphabet}

for char in text:
    if char in english_alphabet:
        letter_count[char] += 1
        total_letters += 1
        
letter_freq = {letter: (count / total_letters) for letter, count in letter_count.items() if count > 0}

sorted_letters = sorted(letter_freq.items(), key=lambda x: (-x[1], x[0]))

with open("analysis.txt", "w") as file:
    for letter, freq in sorted_letters:
        file.write(f"{letter} {freq:.3f}\n")
""" 
        