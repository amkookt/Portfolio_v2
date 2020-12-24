from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class About(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    description = models.TextField(max_length=8000,null=True, blank=True)
    about_image  = models.ImageField(upload_to='media/about',null=True, blank=True)
    

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("about")

class Service(models.Model):
    title_service = models.CharField(max_length=200,null=True, blank=True)
    about_service = models.TextField(max_length=8000,null=True, blank=True)
    image_service  = models.ImageField(upload_to='media/service',null=True, blank=True)

    def __str__(self):
        return self.title_service
    def get_absolute_url(self):
        return reverse("home")


class Project(models.Model):
    title = models.CharField(max_length=200,null=True, blank=True)
    author = models.ForeignKey(User,default=1, on_delete=models.CASCADE)
    languages = models.CharField(max_length=800)
    description = models.TextField(max_length=8000,null=True, blank=True)
    image  = models.ImageField(upload_to='media/service',null=True, blank=True)
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse("home")







