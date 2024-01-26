import random

def generate_random_hex_color(count: int = 1):
    result = []
    for _ in range(count):
        color = generate_random_hex_color_inner()
        result.append(color)
    return result

def generate_random_hex_color_inner():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF)).upper()
    return color