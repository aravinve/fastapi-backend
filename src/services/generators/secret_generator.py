import secrets
import string

def generate_random_secure_text(count: int = 1, length: int = 10):
    result = []
    for _ in range(count):
        secret = generate_random_secure_text_inner(length)
        result.append(secret)
    return result

def generate_random_secure_text_inner(length: int = 10):
    permitted_special_characters = '@#$%^&*'
    characters = string.ascii_letters + string.digits + permitted_special_characters
    return ''.join(secrets.choice(characters) for _ in range(length))
    
