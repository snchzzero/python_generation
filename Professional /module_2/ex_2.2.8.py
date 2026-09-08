
def corporation_mail():
    already_count_mail = int(input())

    already_mails_d = {}

    for _ in range(already_count_mail):
        mail = input()
        name_draft = mail.split('@')[0]
        num = ''
        for i in range(-1, -len(name_draft) + 1, -1):

            if name_draft[i].isdigit() or name_draft[i] == '0':
                num += name_draft[i]
                continue

            if i == -1:
                name = name_draft[-len(name_draft):]
            else:
                name = name_draft[-len(name_draft):i+1]

            if name not in already_mails_d:
                already_mails_d[name] = []
            num = 0 if num == '' else int(num[-1::-1])
            already_mails_d[name].append(num)
            already_mails_d[name].sort()
            break


    result = []
    for _ in range(int(input())):
        new_user = input()
        if new_user in already_mails_d:
            new_number = already_mails_d[new_user][-1]
            miss_number = None
            for numb in range(new_number):
                if numb not in already_mails_d[new_user]:
                    miss_number = numb
                    already_mails_d[new_user].append(numb)
                    already_mails_d[new_user].sort()
                    break
            if miss_number is None and miss_number != 0:
                miss_number = new_number + 1
                already_mails_d[new_user].append(miss_number)
                already_mails_d[new_user].sort()
            miss_number = '' if miss_number == 0 else miss_number

            result.append(f'{new_user}{miss_number}@beegeek.bzz')
        else:
            result.append(f'{new_user}@beegeek.bzz')
            already_mails_d[new_user] = [0]

    return result



for _ in corporation_mail():
    print(_)
