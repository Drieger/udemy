import os
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_one.settings")

import django
django.setup()

from first_app.models import AccessRecord, Webpage, Topic
from faker import Faker

fake = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():
    t = Topic.objects.get_or_create(topic_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        topic = add_topic()
        fake_url = fake.url()
        fake_date = fake.date()
        fake_name = fake.company()

        webpage = Webpage.objects.get_or_create(topic=topic, url=fake_url, name=fake_name)[0]
        accessrecord = AccessRecord.objects.get_or_create(name=webpage, date=fake_date)[0]

if __name__ == '__main__':
    print("Populating database")
    populate(20)
    print("Database completely populated")
