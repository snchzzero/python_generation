def translate(people_count: int) -> str:
    languages = [
        {*input().split(', ')}
        for _ in range(people_count)
    ]
    intersection_ = languages[0]
    for person_languages in languages:
        intersection_ = intersection_.intersection(person_languages)
    if intersection_:
        return ', '.join(sorted(
            [lang for lang in  intersection_], key=lambda lang: lang[0]
        ))
    return 'Сериал снять не удастся'




print(translate(int(input())))