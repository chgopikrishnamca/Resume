from django.db import models
from django.db.models.fields import URLField

# Model classes for defining portfolio

class Skill(models.Model):
    title = models.CharField(max_length=100)
    skill1 = models.CharField(max_length=250, default="")
    skill2 = models.CharField(max_length=250, default="", blank=True)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class DevOps(models.Model):
    title = models.CharField(max_length=100)
    skill1 = models.CharField(max_length=250, default="")
    skill2 = models.CharField(max_length=250, default="", blank=True)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Interest(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250, default="")
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

