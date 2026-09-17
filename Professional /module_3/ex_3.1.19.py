from datetime import date
florida_hurricane_dates = [
    date(1987, 11, 15),
    date(1988, 3, 12),
    date(1980, 6, 1),
    date(1980, 5, 31),
    date(1976, 5, 12)
]

# счетчик для нужного количества ураганов
early_hurricanes = 0

# цикл по датам в которые был ураган
for hurricane in florida_hurricane_dates:
    # если месяц урагана меньше чем июнь (порядковый номер 6)
    if hurricane.month < date(1950, 6, 1).month:
        early_hurricanes += 1

print(early_hurricanes)