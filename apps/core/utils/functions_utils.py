# Utils function file
import random
import string

def generate_random_code(length=8):
    """ Generate and return string with 8 characteres """

    try:
        if length < 1:
            raise ValueError("Length must be a positive integer")

        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    except Exception:
        raise Exception('Error at generate code')
