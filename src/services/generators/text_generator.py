import random
import string


def generate_random_text(count: int = 1, length: int = 1, letters: bool = True, digits: bool = False, punctuation: bool = False, whitespace: bool = False):
    result = []
    for _ in range(count):
        random_text = generate_random_text_inner(length, letters, digits, punctuation, whitespace)
        result.append(random_text)
    return result

def generate_random_text_inner(length: int = 1, letters: bool = True, digits: bool = False, punctuation: bool = False, whitespace: bool = False):
    characters = ""
    if letters:
        characters = characters + string.ascii_letters
    if digits:
        characters = characters + string.digits
    if punctuation:
        characters = characters + string.punctuation
    if whitespace:
        characters = characters + string.whitespace
    return ''.join(random.choice(characters) for _ in range(length))
