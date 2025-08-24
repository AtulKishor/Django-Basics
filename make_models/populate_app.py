import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'make_models.settings')

import django
django.setup()

import random
from my_first_app.models import AccessRecord, Topic, WebPage
from faker import Faker

fake_gen = Faker()

topics = ["Social", "Marketplace", "Search", "News", "Games", "Yoga"]

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        # get a topic for entry
        top = add_topic()

        # create fake data for that entry
        fake_url = fake_gen.url()
        fake_date = fake_gen.date()
        fake_name = fake_gen.company()

        # create a new fake web page entry
        webpg = WebPage.objects.get_or_create(topic = top, name=fake_name, url = fake_url)[0]

        # create a fake access record for that web page
        acc_rec = AccessRecord.objects.get_or_create(name=webpg, date = fake_date)[0]


if __name__=='__main__':
    print('popultaing script')
    populate(10)
    print("population complete.")