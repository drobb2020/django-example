from datetime import date, datetime

from django.db import models
from ckeditor.fields import RichTextField

class Author(models.Model):
    name = models.CharField(max_length=250)
    drobb2011@gmail.com = models.CharField(max_length=250)
    bio = RichTextField(null=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile/', null=True, blank=True)
    social_drobb2011@gmail.com = models.CharField(max_length=250, blank=True, null=True)
    social_github = models.CharField(max_length=250, blank=True, null=True)
    social_facebook = models.CharField(max_length=250, blank=True, null=True)
    social_linkedin = models.CharField(max_length=250, blank=True, null=True)
    social_twitter = models.CharField(max_length=250, blank=True, null=True)
    social_website = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return f"{self.name} {self.drobb2011@gmail.com}"


class Post(models.Model):
    title = models.CharField(max_length=250)
    date = models.DateTimeField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    snippet = models.CharField(max_length=250, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    post_img = models.ImageField(upload_to='post/', null=True, blank=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.author.name}"
