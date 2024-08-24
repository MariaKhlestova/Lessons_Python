# Практическая работа. Семинар 3. Списки и словари.

sp = list()
sp = [-1, True, "Hello", 5.77, 8.999, "world"]
"""
print(sp)
print(sp[2:5])

for i in range(len(sp)):
    print(f"{i} - {sp[i]}")

for el in sp:
    print(el, end = ' ')
print(end = '\n')

sp.append('last') # добавляет элемент в конец
sp.insert(0, 'first') # добавляет в любое место
# print(sp)

sp.remove(True)
del sp[0]
# print(sp)

a = sp.pop()
# print(a)
# print(sp)
"""

# Кортежи (удобно передавать данные между приложениями, настройки)
t = tuple(sp)
# print(t)
# print('Hi' in t)
# print('Hello' in t)

d = {}
d['дядя Ваня'] = 868686
d['дядя Вася'] = 212121
# print(d)
# print(list(d.keys()))
# print(d.keys()) # хотим получить информацию обо всех ключах
# print(d.values()) # хотим получить информацию о значениях
# for i in d:
#    print(i)
# for key, value in d.items(): # метод items()
#    print(f"{key} - {value}")

# Множество
"""
s = {1,1,1,1,5,5,8,8,8,8,8}

s.add(7)
s.discard(1)
s.discard(2)

print(s)

"""
# Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) 
# на K элементов вправо, K – положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

# k = int(input('Введите число k: '))
# s = [1, 2, 3, 4, 5]

# for _ in range (k) :
#    s.insert(0, s.pop())

# print(s)

# k = int(input('Введите число k: '))
# s = [1, 2, 3, 4, 5]

# print (f"[{*s[k+1:], *s[:k+1]}]")
