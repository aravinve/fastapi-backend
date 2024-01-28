import faker
from src.models.generator_models import FakerCategory

fake = faker.Faker()

def generate_random(fakerCategory: FakerCategory, count: int = 1):
    result = []
    for _ in range(count):
        if fakerCategory is FakerCategory.username:
            random_value = generate_random_name()
        if fakerCategory is FakerCategory.address:
            random_value = generate_random_addr()
        if fakerCategory is FakerCategory.firstname:
            random_value = generate_random_firstname()
        if fakerCategory is FakerCategory.lastname:
            random_value = generate_random_lastname()
        if fakerCategory is FakerCategory.email:
            random_value = generate_random_email()
        if fakerCategory is FakerCategory.phone_number:
            random_value = generate_random_phone_number()
        if fakerCategory is FakerCategory.date_of_birth:
            random_value = generate_random_date_of_birth()
        if fakerCategory is FakerCategory.company:
            random_value = generate_random_company()
        if fakerCategory is FakerCategory.word:
            random_value = generate_random_word()
        if fakerCategory is FakerCategory.sentence:
            random_value = generate_random_sentence()
        if fakerCategory is FakerCategory.paragraph:
            random_value = generate_random_paragraph()
        if fakerCategory is FakerCategory.text:
            random_value = generate_random_text()
        if fakerCategory is FakerCategory.emoji:
            random_value = generate_random_emoji()
        if fakerCategory is FakerCategory.date:
            random_value = generate_random_date()
        if fakerCategory is FakerCategory.profile:
            random_value = generate_random_profile()
        if fakerCategory is FakerCategory.location:
            random_value = generate_random_latlng()
        if fakerCategory is FakerCategory.currency:
            random_value = generate_random_currency()
        
        result.append(random_value)
    return result

def generate_random_name():
    return fake.name()
    
def generate_random_addr():
    return fake.address()

def generate_random_firstname():
    return fake.first_name()

def generate_random_lastname():
    return fake.last_name()

def generate_random_email():
    return fake.email()

def generate_random_phone_number():
    return fake.phone_number()

def generate_random_date_of_birth():
    return fake.date_of_birth()

def generate_random_company():
    return fake.company()

def generate_random_word():
    return fake.word()

def generate_random_sentence():
    return fake.sentence()

def generate_random_paragraph():
    return fake.paragraph()

def generate_random_text():
    return fake.text()

def generate_random_emoji():
    return fake.emoji()

def generate_random_date():
    return fake.date()

def generate_random_profile():
    return fake.profile()

def generate_random_latlng():
    return fake.latlng()

def generate_random_currency():
    return fake.currency()
