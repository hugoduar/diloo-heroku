from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Critic(models.Model):
    user = models.OneToOneField(User)
    display_name = models.CharField(max_length=50)
    readers = models.ManyToManyField("self", blank=True)
    to_read = models.ManyToManyField("self", blank=True)
    image = image = models.CharField(max_length=300)
    class Meta:
		verbose_name_plural = "Critics"
    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    class Meta:
		verbose_name_plural = "Categories"
    def __unicode__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
    class Meta:
		verbose_name_plural = "Topics"
    def __unicode__(self):
        return self.name

class Review(models.Model):
    content = models.CharField(max_length=1000)
    topics = models.ManyToManyField(Topic, blank=True)
    title = models.CharField(max_length=100)
    critic = models.ForeignKey(Critic)
    avg = models.FloatField()
    readings = models.IntegerField()
    class Meta:
		verbose_name_plural = "Reviews"
    def __unicode__(self):
        return self.critic.user.username + ' - ' + self.content
