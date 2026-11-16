"""

5
2021-08-01
2021-08-02
2021-07-01
2021-06-01
2021-05-01

"""

from datetime import date

def sorted_dates():
    dates = sorted([date.fromisoformat(input()) for _ in range(int(input()))])
    for date_ in dates:
        print(date_.strftime('%d/%m/%Y'))


sorted_dates()