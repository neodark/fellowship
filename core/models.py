#from django.db import models
from datetime import datetime

# Create your models here.
from django.core.urlresolvers import reverse

#from mongoengine import ListField, EmbeddedDocumentField
from mongoengine import *
from mongoengine.django.auth import User

class Tag(Document):
	title = StringField(max_length=200, required=True)

	def __unicode__(self):
		return self.title

	def posts_count(self):
		return len(Post.objects(tags=self.id))

	def posts_avg_length(self):
		return Post.objects(tags=self.id).average('text_length')

class Post(Document):
    created_at = DateTimeField(default=datetime.now)
    title = StringField(max_length=255, required=True)
    slug = StringField(required=True)
    body = StringField()
    comments = ListField(EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return reverse('post', kwargs={"slug": self.slug})

    def __unicode__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]


class Comment(Document):
    created_at = DateTimeField(default=datetime.now)
    body = StringField(verbose_name="Comment")
    author = StringField(verbose_name="Name", max_length=255)
