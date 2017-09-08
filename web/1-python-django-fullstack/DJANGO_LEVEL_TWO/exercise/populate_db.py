import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "exercise.settings")

import django
django.setup()

from users.models import User
from faker import Faker

fake = Faker()

def populate(N=5):
    for entry in range(N):
        first = fake.first_name()
        last = fake.last_name()
        email = fake.email()
        user = User.objects.get_or_create(first_name=first, last_name=last, email=email)[0]
        user.save()


if __name__ == '__main__':
    print("Populating database")
    populate(20)
    print("Database completely populated")
