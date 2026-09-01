rules_map = {
    '0': 'yellow',
    '1': 'green',
    '2': 'red',
    '3': 'red',
    '4': 'red',
    '5': 'yellow',
    '6': 'yellow',
    '7': 'yellow',
    '8': 'yellow',
    '9': 'yellow',
    '10': 'yellow',
    '11': 'yellow',
    '12': 'yellow',
    '13': 'yellow',
    '14': 'yellow',
    '15': 'yellow',
    '16': 'yellow',
    '17': 'yellow',
    '18': 'yellow',
    '19': 'yellow'
}

def choose_plural(amount: int, declensions: tuple):

    green, red, yellow  = declensions
    declensions_map = {
        'green': green,
        'red': red,
        'yellow': yellow
    }

    rule = ''
    if amount >= 11:
        last_chars = str(amount)[-2:]
        rule = rules_map.get(last_chars, '')
    if not rule:
        last_char = str(amount)[-1]
        rule = rules_map.get(last_char, '')

    result = f'{amount} {declensions_map.get(rule)}'
    return result

print(choose_plural(1223123111, ('пример', 'примера', 'примеров')))
print(choose_plural(21, ('пример', 'примера', 'примеров')))
print(choose_plural(92, ('гвоздь', 'гвоздя', 'гвоздей')))

print(choose_plural(8, ('яблоко', 'яблока', 'яблок')))
print(choose_plural(111, ('пример', 'примера', 'примеров')))
print(choose_plural(2, ('пример', 'примера', 'примеров')))
print(choose_plural(3458438435812, ('доллар', 'доллара', 'долларов')))
print(choose_plural(11, ('стул', 'стула', 'стульев')))
print(choose_plural(666, ('шкаф', 'шкафа', 'шкафов')))
print(choose_plural(505, ('утка', 'утки', 'уток')))
print(choose_plural(49324, ('плюмбус', 'плюмбуса', 'плюмбусов')))
print(choose_plural(512312, ('цент', 'цента', 'центов')))