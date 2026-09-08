A_CHARS = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']

def equal_words(target_word: str, count: str) -> list:
    words = [
        input()
        for _ in range(int(count))
    ]
    target_word_d = {}
    for i in range(len(target_word)):
        if target_word[i] in A_CHARS:
            target_word_d[i] = target_word[i]
    target_word_s = set(target_word_d.keys())

    result = []
    for word in words:
        indexes = set()
        for i in range(len(word)):
            if word[i] in A_CHARS:
                indexes.add(i)
        if indexes == target_word_s:
            result.append(word)
    return result



for res in equal_words(input(), input()):
    print(res)