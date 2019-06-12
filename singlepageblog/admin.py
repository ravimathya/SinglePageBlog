from django.contrib import admin
from .models import Tag, Blog

# Register your models here.


class BlogModelAdmin(admin.ModelAdmin):
    list_filter = ["tag"]

    class Meta:
        model = Blog


admin.site.register(Blog)
admin.site.register(Tag)
