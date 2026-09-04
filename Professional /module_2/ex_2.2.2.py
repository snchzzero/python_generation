
rus_alpha = [i for i in "АаВСсЕеНКМОоРрТХху"]
eng_alpha = [i for i in "AaBCcEeHKMOoPpTXxy"]

def ru_eng():
    a1 = str(input())
    b1 = str(input())
    c1 = str(input())
    a = 'ru' if a1 in rus_alpha else 'en'
    b = 'ru' if b1 in rus_alpha else 'en'
    c = 'ru' if c1 in rus_alpha else 'en'
    if len({a, b, c}) == 1:
        return list({a, b, c})[0]
    else:
        return 'mix'

print(ru_eng())
