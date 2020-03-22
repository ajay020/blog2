import os,django,random
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', "mysite.settings")
django.setup()

from faker import Faker
from blog.models import Post
from django.contrib.auth.models import User
from django.utils import timezone

def create_post(N):
    fake = Faker()
    for _ in range(N):
        id = random.randint(1,4)
        title = fake.name()
        status = random.choice(['published','draft'])
        Post.objects.create(
        title = title + ' Post!!',
        author = User.objects.get(id=id),
        slug = '-'.join(title.lower().split()),
        body = fake.text(),
        created = timezone.now(),
        updated  = timezone.now()

        )

print("DATA IS POPULATED SUCCESSFULLY!.")
create_post(10)
