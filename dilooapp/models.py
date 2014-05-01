from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Critic(models.Model):
    user = models.OneToOneField(User)
    display_name = models.CharField(max_length=50)
    readers = models.ManyToManyField("self", blank=True)
    to_read = models.ManyToManyField("self", blank=True)
    image = image = models.CharField(max_length=300)

    def __unicode__(self):
        return self.user.username


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    
    def __unicode__(self):
        return self.name


class Thing(models.Model):
    category = models.ForeignKey(Category)
    critic = models.ForeignKey(Critic)
    name = models.CharField(max_length=140)
    description = models.CharField(max_length=500)
    dateCreated = models.DateTimeField('pub_date')

    def __unicode__(self):
        return self.name


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name


class Review(models.Model):
    content = models.CharField(max_length=1000)
    topics = models.ManyToManyField(Topic, blank=True)
    thing = models.ForeignKey(Thing)
    critic = models.ForeignKey(Critic)
    avg = models.FloatField()
    readings = models.IntegerField()

    def __unicode__(self):
        return self.thing.name + ' - ' + self.content


class Comment(models.Model):
    content = models.CharField(max_length=1000)
    review = models.ForeignKey(Review)
    critic = models.ForeignKey(Critic)

    def __unicode__(self):
        return self.critic.username


class Note(models.Model):
    GOOD = 3
    REGULAR = 2
    BAD = 1

    NOTE_CHOICE = (
        (GOOD, 3),
        (REGULAR, 2),
        (BAD, 1)
    )
    note = models.IntegerField(choices=NOTE_CHOICE)
    critic = models.ForeignKey(Critic)
    review = models.ForeignKey(Review)

    def __unicode__(self):
        return self.critic.user.username + ' - ' + str(self.note)
