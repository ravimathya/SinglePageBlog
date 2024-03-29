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
    slug = models.SlugField(unique=True, blank=True, null=True)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None)
    date = models.DateTimeField()
    image = models.ImageField(
        upload_to='blog/', default='default.jpg', blank=True, null=True)
    content = models.TextField(default=None)
    draft = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("singlepageblog:blogDetail", kwargs={"slug": self.slug})

    class Meta:
        ordering = ["-date"]
        verbose_name = "My Blog"
        verbose_name = "My Blogs"


def create_slug(instance, new_slug=None):
    slug = slugify(instance.title)
    if new_slug is not None:
        slug = new_slug
    qs = Blog.objects.filter(slug=slug).order_by("-id")
    exits = qs.exists()
    if exits:
        # to make it unique
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug


def pre_save_post_receiver(sender, instance, *args, **kwargs):
    instance.slug = create_slug(instance)
    # do other stuffs here


pre_save.connect(pre_save_post_receiver, sender=Blog)
