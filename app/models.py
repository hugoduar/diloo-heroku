from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Critic(models.Model):
    user = models.OneToOneField(User)
<<<<<<< HEAD
    readers = models.ManyToManyField("self", blank=True)
    to_read = models.ManyToManyField("self", blank=True)
    display_name = models.CharField(max_length=50)
    image = image = models.CharField(max_length=300)
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    class Meta:
        verbose_name_plural = "Critics"
=======
    display_name = models.CharField(max_length=50)
    readers = models.ManyToManyField("self", blank=True)
    to_read = models.ManyToManyField("self", blank=True)
    image = image = models.CharField(max_length=300)
    class Meta:
		verbose_name_plural = "Critics"
>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f
    def __unicode__(self):
        return self.user.username

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
<<<<<<< HEAD
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    class Meta:
        verbose_name_plural = "Categories"
=======
    class Meta:
		verbose_name_plural = "Categories"
>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f
    def __unicode__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=100)
<<<<<<< HEAD
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    class Meta:
        verbose_name_plural = "Topics"
    def __unicode__(self):
        return self.name

class Score(models.Model):
    critic = models.ForeignKey(Critic)
    avg = models.IntegerField()
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    class Meta:
        verbose_name_plural = "Scores"
    def __unicode__(self):
        return self.critic.user.username + ' - ' + self.avg

class Review(models.Model):
    critic = models.ForeignKey(Critic)
    category = models.ForeignKey(Category)
    topics = models.ManyToManyField(Topic, blank=True)
    scores = models.ManyToManyField(Score, blank=True)
    pre_content = models.TextField()
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now=True, auto_now_add=True)
    title = models.CharField(max_length=100) 
    readings = models.IntegerField()
    class Meta:
        verbose_name_plural = "Reviews"
=======
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
>>>>>>> e64198d1ec8ab66b34da6f833eb5cba7f22bea9f
    def __unicode__(self):
        return self.critic.user.username + ' - ' + self.content
