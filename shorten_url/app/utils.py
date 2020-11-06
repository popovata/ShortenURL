import random
import string

letters_and_digits = string.ascii_letters + string.digits
SHORT_KEY_LENGTH = 5

def get_random_alphanumeric_string(length):
    return ''.join((random.choice(letters_and_digits) for i in range(length)))
