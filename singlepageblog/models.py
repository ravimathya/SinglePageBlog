from django.db import models
from django.conf import settings
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.urls import reverse

# Create your models here.


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("singlepageblog:tagBlog", kwargs={"name": self.name})


class Blog(models.Model):
    title = models.CharField(max_length=200, unique=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField()
    image = models.ImageField(
        upload_to='blog/', default='default.jpg', blank=True, null=True)
    content = models.TextField(default=None)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title
