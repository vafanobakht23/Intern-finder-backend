import string
from django.utils import timezone

def generate_random_string(length):
    printable = string.ascii_letters + string.digits
    random_password = "".join(secrets.choice(printable) for _ in range(length))
    return random_password

def now():
    return timezone.now()
