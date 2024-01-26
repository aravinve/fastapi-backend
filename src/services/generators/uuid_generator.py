from uuid import uuid4

def generate_random_uuids(count: int, hyphens: bool, uppercase: bool):
    result = []
    for _ in range(count):
        generated_uuid_value = str(uuid4())
        if not hyphens:
            generated_uuid_value = generated_uuid_value.replace("-", "")
        if uppercase:
            generated_uuid_value = generated_uuid_value.upper()
        result.append(generated_uuid_value)
    return result