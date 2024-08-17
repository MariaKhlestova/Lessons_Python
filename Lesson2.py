# num = int(input("Введите число "))
#проверим что ввел пользователь
"""
if num % 2 == 0:
    print("Вы ввели четное число ")
if num % 2 == 1:
    print("Вы ввели нечетное число ")
"""
# упростим код
"""
if num % 2 == 0:
    print("Вы ввели четное число ")
elif num == 0:
    print("Вы ввели 0 ")
else:
    print("Вы ввели нечетное число ")
"""   
"""
for i in range(10):
    num = int(input("Введите число "))
    if num == 0:
        print("Вы ввели ноль ")
    elif num % 2 == 0:
        print(" Вы ввели четное число ")
    else:
        print("Вы ввели нечетное число ")
"""
"""
while True:
    num = int(input("Введите число для анализа, для выхода из цикла введите ноль "))
    if num == 0:
        print("Вы ввели ноль ")
        break
    elif num % 2 == 0:
        print(" Вы ввели четное число ")
    else:
        print("Вы ввели нечетное число ")
"""
# Задача 1: По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N 
# (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input: 5
# Output: 120
"""
n = int(input("Введите целое неотрицательное число n: "))
a = 1
for i in range (1, n+1):
    a*=i
print(a)

"""
# Задача 2: Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть 
# выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

"""
a = int(input('Введите число: '))
d1 = 1
d2 = 0
current = d1 + d2
n = 3
while current < a:
    n += 1
    d2 = d1
    d1 = current
    current = d1 + d2

if a != current:
    print('-1')
else:
    print('n=', n)
"""
# Задача 3: Уставшие от необычно теплой зимы, жители решили узнать, действительно ли это самая длинная оттепель 
# за всю историю наблюдений за погодой. Они обратились к синоптикам, а те, в свою очередь, занялись исследованиями 
# статистики за прошлые годы. Их интересует, сколько дней длилась самая длинная оттепель. 
# Оттепелью они называют период, в который среднесуточная температура ежедневно (несколько дней подряд!) превышала 0 градусов Цельсия. 
# Напишите программу, помогающую синоптикам в работе. 
# Пользователь вводит число N – общее количество рассматриваемых дней (1 ≤ N ≤ 100). 
# В следующих строках располагается N целых чисел. Каждое число – среднесуточная температура в соответствующий день. 
# Температуры – целые числа и лежат в диапазоне от –50 до 50
# Input: 6 -> -20 30 -40 50 10 -10
# Output: 2
"""
d = int(input("Введите число рассматриваемых дней: "))
d1 = 0
dmax = 0
for i in range (d):
    temp = int(input("Введите значение температуры: "))
    if temp > 0:
        d1 += 1
        if d1 > dmax:
           dmax = d1
    else:
        d1 = 0
print(dmax)
"""
# Дополнительное задание:
# Пользователь вводит любое число (дробное или целое), надо посчитать количество цифр в числе. 
# Решаем строго математически, обращаться к числу как к строке нельзя.
# 0 -> 1
# 9 -> 1
# 56.77 -> 4
# -0.0001 - > 5
# 100.18006 ->8
"""
a = input("Введите число: ")
a1 = "".join(c for c in a if  c.isdecimal()) # исключили все символы кроме цифр
print(len(a1)) # считаем длину строки

"""
# Дополнительное задание:
# Валентина прогуляла лекцию по математике. Преподаватель решил подшутить над нерадивой студенткой и 
# попросил ее на практическом занятии перечислить все положительные делители некоторых целых чисел. 
# Для несложных примеров студентка быстро нашла решения (для числа 6 это: 1, 2, 3, 6; а для числа 16 это: 1, 2, 4, 8, 16), но этим все не закончилось. 
# На домашнее задание ей дали варианты посложнее: 23436, 190187200, 380457890232. 
# Решить такое вручную, как вы понимаете, практически нереально.
# Вот Валентина и обратилась к вам за помощью. Помогите ей.

"""
n = int(input("Введите число: "))

for i in range(1, n):

   if n % i == 0:

       print(i,end=" ")
"""
# Практические задания
# Задача 1: Поставьте оценку!
# Вася выложил своё новое приложение на платформу для начинающих разработчиков,
# на ней пользователи могут ставить оценку приложению: от −100 до 100. Ему
# захотелось сравнить количество положительных и отрицательных отзывов, для этого
# он заранее отфильтровал все отзывы так, чтобы в конце были те, которые равны нулю.
# Напишите программу, которая находит количество положительных и количество
# отрицательных чисел в последовательности. Последовательность заканчивается на числе 0.
"""
nice_count = 0
bed_count = 0
n = 1
while n != 0:
    n = int(input("Введите оценку: "))
    if n > 0:
        nice_count += 1
    elif n < 0:
        bed_count += 1
    elif n == 0:
        break
print("Количество положительных отзывов: ", nice_count)
print("Количество отрицательных отзывов: ", bed_count)
"""
# Задача 2: Обычный день на работе
# Максим программирует целый день на работе и вечером идёт домой. Каждый час начальство кидает ему несколько задач, 
# которые нужно решить до следующего рабочего часа. Вдобавок каждый час Максиму звонит супруга. Он знает, что если он
# возьмёт трубку, то жена попросит зайти вечером в магазин.
# Напишите программу, в которой считается, сколько задач выполнил Максим за день (восемь часов). 
# Если он хотя бы раз взял трубку, то в конце дополнительно выводите сообщение: «Нужно зайти в магазин».
"""
t = 0
tasks_sum = 0
go_to_store = False

print("Начался 8-часовой рабочий день")
while t != 8:
    t += 1
    print(t, "час")
    tasks = int(input("Сколько задач решит Максим? "))
    tasks_sum += tasks
    call = int(input("Звонит жена. Взять трубку? (1 - да, 0 - нет): "))
    if call == 1:
        go_to_store = True
print("Рабочий день закончен. Всего выполнено задач: ", tasks_sum)
if go_to_store:
    print("Нужно зайти в магазин.")
"""
# Задача 3: Игра "Угадай число"
# Папа-программист написал для сына программу, которая просит его угадать число. Недостаток программы был в том, 
# что бедному сыну приходилось её каждый раз перезапускать, чтобы угадывать число. Теперь, когда мы знаем гораздо больше, 
# пришло время исправить этот недостаток и заодно немного улучшить саму игру.
# Напишите программу-игру, которая запрашивает у пользователя число до тех пор, пока он его не отгадает. 
# Выводите сообщения в соответствии с примером.
"""
number = int(input("Введите загаданное число: "))
guess_count = 0
while True:
    guess_num = int(input("Введите число: "))
    guess_count += 1
    if guess_num > number:
        print("Число больше, чем нужно. Попробуйте ещё раз!")
    elif guess_num < number:
        print("Число меньше, чем нужно. Попробуйте ещё раз!")
    else:
        print("Вы угадали! Число попыток:", guess_count)
        break
"""
# Задача 4: Посчитай чужую зарплату...