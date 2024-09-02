# Задача 1. Поиск элемента
"""
def find_key(struct, key, max_depth=None, depth=1):
    result = None
    
    if max_depth and max_depth < depth:
        return result
    
    if key in struct:
        return struct[key]
    
    for sub_struct in struct.values():
        if isinstance(sub_struct, dict):
            result = find_key(sub_struct, key, max_depth, depth=depth+1)
            if result:
                break
    return result

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

while True:
    key = input('Введите искомый ключ: ')
    answer = input('Хотите ввести максимальную глубину? Y/N: ')
    
    if answer.lower() == 'y':
        max_depth = int(input('Введите максимальную глубину: '))
    else:
        max_depth = None
        
    print('Значение ключа: ', find_key(struct=site, max_depth=max_depth, key=key))
"""
# Задача 2. Глубокое копирование
"""
import copy

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

def change_value(struct, key, value):
    if key in struct:
        struct[key] = value
        
    else:
        for sub_struct in struct.values():
            if isinstance(sub_struct, dict):
                change_value(sub_struct, key, value)
    return struct

def display_struct(struct, spaces=1):
    for key, value in struct.items():
        if isinstance(value, dict):
            print(' ' * spaces, key)
            display_struct(value, spaces + 3)
        else:
            print("{}{} : {}".format(' ' * spaces, key, value))
            
def make_site(name):
    struct_site = copy.deepcopy(site)
    new_title = 'Куплю/продам {} недорого'.format(name)
    struct_site = change_value(struct_site, 'title', new_title)
    new_h2 = 'У нас самая низкая цена на {}'.format(name)
    struct_site = change_value(struct_site, 'h2', new_h2)
    return struct_site

sites = []
sites_count = int(input('Сколько сайтов: '))

for _ in range(sites_count):
    product_name = input('Введите название продукта для нового сайта: ')
    new_site = make_site(product_name)
    sites.append(new_site)
    
    for i_site in sites:
        display_struct(i_site)
"""
# Задача 3. Продвинутая функция sum
"""
def my_sum(*args):
    total_sum = 0
    
    for i_elem in args:
        if isinstance(i_elem, int):
            total_sum += i_elem
        elif isinstance(i_elem, (list, tuple)):
            for x in i_elem:
                total_sum += my_sum(x)
    return total_sum
# код для тестирования
print(my_sum([[1, 2, [3]], [1], 3]))
print(my_sum(1, 2, 3, 4, 5))
"""
# Задача 4. Список списков

def flatten(a_list):
    result = []
    
    for e in a_list:
        if isinstance(e, int):
            result.append(e)
        else:
            result.extend(flatten(e))
    return result

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]
flattened_list = flatten(nice_list)

print(flattened_list)

            