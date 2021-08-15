from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='project_pics')
    created = models.DateTimeField(auto_now=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title


class Blog(models.Model):
    title = models.CharField(max_length=100, null=True)
    content = models.TextField()
    image = models.ImageField(default='default.jpg', upload_to='blog_pics')
    created = models.DateTimeField(auto_now=timezone.now, blank=True, null=True)

    def __str__(self):
        return self.title
