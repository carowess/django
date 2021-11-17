import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","learning_log.settings")

import django
django.setup()

from MainApp.models import Topic, Entry

topics = Topic.objects.all()
# exactly like saying 'select * from Topic' in SQL

for topic in topics:
    print(topic.id)
    print(topic.text) #can also just say 'print(topic)' and it gets the same output 
    print(topic.date_added)

t = Topic.objects.get(id=1)
print(t)

## to get all the entries for a specific topic
entries = t.entry_set.all()

for e in entries:
    print(e)