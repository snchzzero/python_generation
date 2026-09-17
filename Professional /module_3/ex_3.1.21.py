from datetime import date

dates = [date(1999, 9, 9)]

def get_min_max(dates_) -> tuple:
    if not dates_:
        return ()
    if len(dates_) == 1:
        return dates_[0], dates_[0]
    else:
        return min(dates_), max(dates_)

print(get_min_max(dates))