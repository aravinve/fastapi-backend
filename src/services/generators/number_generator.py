import random
import sys

def generate_random_numbers(count: int = 1, min: int = -sys.maxsize - 1, max: int = sys.maxsize):
    result = []
    for _ in range(count):
        random_number = generate_random_number_inner(min, max)
        result.append(random_number)
    return result

def generate_random_number_inner(min: int, max: int):
    return random.randint(min, max)