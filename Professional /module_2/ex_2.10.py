from copy import deepcopy


def filter_anagrams(word: str, words: list) -> list:
    result = []

    char_list = [char for char in word]

    for word_ in words:
        char_list_ = deepcopy(char_list)
        for char_ in word_:
            if char_ in char_list_:
                char_list_.remove(char_)
            else:
                break
        if not char_list_:
            result.append(word_)
    return result





print(filter_anagrams('клоун', ['колдун', 'кулон', 'уклон', 'кол']))
