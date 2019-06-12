from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from.models import Blog, Tag

# Create your views here.


def index(request):
    blog_list = Blog.objects.all()
    tag_list = Tag.objects.all()
    context = {
        # to dispaly in front-end, we first make list and then context by adding like story_list and tag_list
        "blog_list": blog_list,
        "tag_list": tag_list
    }
    return render(request, 'blog/blog.html', context)


def blog_detail(request, slug=None):
    # Blog is model and slug is used for query.
    instance = get_object_or_404(Blog, slug=slug)
    context = {
        "instance": instance
    }
    return render(request, 'blog/blogDetail.html', context)


def blog_tag(request, name=None):
    blog_list = Blog.objects.filter(tag__name=name)
    tag_list = Tag.objects.all()
    context = {
        "blog_list": blog_list,
        "name": name,
        "tag_list": tag_list

    }
    return render(request, 'blog/tag-blog.html', context)
