
def hide_card(card_number: str) -> str:

    new_card_number = ''
    for char in card_number:
        if char.isdigit():
            if len(new_card_number) < 12:
                new_card_number += '*'
            else:
                new_card_number += char
    return new_card_number



card = '905 678123 45612 56'
print(hide_card(card))


