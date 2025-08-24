import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fifth.settings')

import django
django.setup()

from modelForms.models import User
from faker import Faker

fake_gen = Faker()

def populate(N=5):
    for entry in range(N):
        # get a topic for entry
        *fake_user_firstname, fake_user_lastname = fake_gen.name().split()
        fake_email = fake_gen.email()
        user = User.objects.get_or_create(first_name = ' '.join(fake_user_firstname), last_name = fake_user_lastname, email= fake_email)[0]
        user.save()

if __name__=='__main__':
    print('popultaing script')
    populate(10)
    print("population complete.")