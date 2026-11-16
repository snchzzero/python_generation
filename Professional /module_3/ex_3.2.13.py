from datetime import date


def is_correct():
    dates = []
    while True:
        input_ = input()
        if input_ == 'end' or input_ == 'end\n':
            break
        dates.append(input_)

    count_correct = 0
    for _ in dates:
        try:
            parsed_date = _.split('.')
            date(int(parsed_date[-1]), int(parsed_date[-2]), int(parsed_date[-3]))
            print('Корректная')
            count_correct += 1
        except Exception:
            print('Некорректная')
    print(count_correct)


is_correct()