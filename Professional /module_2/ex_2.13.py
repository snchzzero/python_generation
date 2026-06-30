def spell(*args):
    if not args:
        return {}

    result = {}
    for arg in args:
        first_letter = str(arg[0]).lower()
        max_length = 0
        for arg_ in args:
            if arg_.lower().startswith(first_letter):
                if len(arg_) > max_length:
                    max_length = len(arg_)
        result[first_letter] = max_length

    return result



words = ['fruit', 'football', 'February', 'forest', 'Family']
print(spell(*words))
