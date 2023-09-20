# Utils function file
import random
import string

def generate_random_code(length=8):
    """ Generate and return string with 8 characteres """

    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
