#from django.db import models
from datetime import datetime

# Create your models here.
from mongoengine import *
from mongoengine.django.auth import User

from core.models import User

class Bubble(Document):
    description = StringField()
    text_length = IntField()
    created_at = DateTimeField(default=datetime.now)
    author = ReferenceField(User)
    attendees = ListField(ReferenceField(User))
    latest = BooleanField(default=True)

    def __unicode__(self):
        return self.description

    def save(self, *args, **kwargs):
        self.text_length = len(self.description)
        return super(Bubble, self).save(*args, **kwargs)
