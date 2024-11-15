import random


def generate_custom_email():
    first_name = "irina"
    last_name = "kurbanova"
    cohort_number = "15"
    random_digits = ''.join(random.choices("0123456789", k=3))
    return f"{first_name}_{last_name}_{cohort_number}_{random_digits}@ya.ru"