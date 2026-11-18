from datetime import datetime
from typing import Optional

file_path = 'diary.txt'

def get_date(line: str) -> Optional[datetime]:
    try:
        return datetime.strptime(line.strip(), '%d.%m.%Y; %H:%M')
    except ValueError:
        return None

def cosmo_book():
    result_dict = {}

    with open(file_path, 'r') as file:
        #lines = file.readlines()
        #print(lines)
        date = None
        for line in file:

            print(line)

            if not date:
                date = get_date(line)
                result_dict[date] = []

            if line == '\n':
                date = None
                continue

            result_dict[date].append(line)
        print(result_dict)
        dates = list(result_dict.keys())
        print(type(dates[0]))
        dates.sort(reverse=True)
        print(dates)
        #new = result_dict.sorted(key=lambda x: x[0], reverse=True)
        #new =sorted(result_dict, key=lambda x: x, reverse=False)
        #print(new)

        dt1 = datetime(2015, 10, 24, 12, 36, 9)
        dt2 = datetime(2015, 11, 24, 12, 36, 9)
        dt3 = datetime(1900, 7, 18)
        dt4 = datetime(2014, 5, 27)
        dt_list = [dt1, dt2, dt3, dt4]

        dt_list.sort(reverse=True)
        print(dt_list)



cosmo_book()