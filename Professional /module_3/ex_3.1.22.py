from datetime import date

date1 = date(2019, 6, 5)
date2 = date(2019, 6, 5)

def get_date_range(date_1, date_2) -> list:
    days_1 = date1.toordinal()
    days_2 = date2.toordinal()
    result = []
    for day in range(days_1, days_2 + 1):
        result.append(date.fromordinal(day))
    return result

print(get_date_range(date1, date2))

