#from django.db import models
from datetime import datetime

# Create your models here.
from mongoengine import *
from mongoengine.django.auth import User

from core.models import User

class Bubble(Document):
    description = StringField()
    created_at = DateTimeField(default=datetime.now)
    author = ReferenceField(User)
    attendees = models.ManyToManyField()

    def __unicode__(self):
        return self.description

