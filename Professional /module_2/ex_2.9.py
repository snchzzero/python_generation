def convert(string: str) -> str:

    count_title = 0
    count_lower = 0
    for char in string:
        if char.istitle():
            count_title +=1
        elif char.islower():
            count_lower += 1
    if count_title > count_lower:
        return string.upper()
    else:
        return string.lower()



print(convert('pi31415!'))





