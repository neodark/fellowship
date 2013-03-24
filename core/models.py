#from django.db import models
from datetime import datetime

# Create your models here.
from django.core.urlresolvers import reverse
from django.core import urlresolvers

#from mongoengine import ListField, EmbeddedDocumentField
from mongoengine import *
from mongoengine.django.auth import User

#class Profile(Document):
#    user = ReferenceField(User)
#    #def set_password(self, raw_password):
#    #    import random
#    #    algo = 'sha1'
#    #    salt = get_hexdigest(algo, str(random.random()), str(random.random()))[:5]
#    #    hsh = get_hexdigest(algo, salt, raw_password)
#    #    self.password = '%s$%s$%s' % (algo, salt, hsh)
#
##class User(Document):
##    last_name = StringField(max_length=255)
##    first_name = StringField(max_length=255)
##
##    def __unicode__(self):
##        return self.last_name+" "+self.first_name

class Tag(Document):
    title = StringField(max_length=200, required=True)

    def __unicode__(self):
        return self.title

    def posts_count(self):
        return len(Post.objects(tags=self.id))

    def posts_avg_length(self):
        return Post.objects(tags=self.id).average('text_length')

class Comment(EmbeddedDocument):
    #created_at = DateTimeField(default=datetime.now)
    text = StringField(verbose_name="Comment")
    author = StringField(verbose_name="Name", max_length=255)

    def __unicode__(self):
        return self.text


class Post(Document):
    created_at = DateTimeField(default=datetime.now)
    date_modified = DateTimeField(default=datetime.now)
    title = StringField(max_length=255, required=True)
    text = StringField(required=True)
    text_length = IntField()
    is_published = BooleanField()
    tags = ListField(ReferenceField(Tag))
    comments = ListField(EmbeddedDocumentField(Comment))

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.text_length = len(self.text)
        return super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('post-detail', args=[self.id])

    def get_edit_url(self):
        return reverse('post-update', args=[self.id])

    def get_delete_url(self):
        return reverse('post-delete', args=[self.id])

    #class Meta:
    #    ordering = ["-created_at"]


