# Практическая работа. Семинар 3. Списки и словари.

sp = list()
sp = [-1, True, "Hello", 5.77, 8.999, "world"]

print(sp)
print(sp[2:5])

for i in range(len(sp)):
    print(f"{i} - {sp[i]}")

for el in sp:
    print(el, end = ' ')
print(end = '\n')