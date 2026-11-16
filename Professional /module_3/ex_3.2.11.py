
from datetime import date


dates = [date(1992, 9, 20), date(1992, 8, 21), date(1992, 7, 22), date(1992, 10, 19)]
def print_good_dates(dates_: list[date]):
    for res in sorted([
        _
        for _ in dates_
        if _.year == 1992 and _.month + _.day == 29
    ]):
        print(res.strftime('%B %d, %Y'))

print_good_dates(dates)