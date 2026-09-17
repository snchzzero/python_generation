from datetime import date

date1 = date(2018, 7, 13)
date2 = date(2018, 7, 13)

def saturdays_between_two_dates(date_1, date_2):
    days_1 = date_1.toordinal()
    days_2 = date_2.toordinal()
    sort_ = sorted([days_1, days_2])

    count_saturdays = 0
    for day in range(sort_[0], sort_[1] + 1):
        if date.fromordinal(day).isoweekday() == 6:
            count_saturdays += 1
    return count_saturdays


print(saturdays_between_two_dates(date1, date2))