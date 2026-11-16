from datetime import date

def compare_dates(date_1_iso, date_2_iso):
    min_date = min([date.fromisoformat(date_1_iso), date.fromisoformat(date_2_iso)])
    return min_date.strftime('%d-%m (%Y)')



print(compare_dates(input(), input()))