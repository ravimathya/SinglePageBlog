from django.urls import path

from . import views

app_name = 'singlepageblog'

urlpatterns = [
    path('', views.index, name='index'),
    path('tag/<str:name>', views.blog_tag, name='tagBlog')
]
