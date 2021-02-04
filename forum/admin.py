from django.contrib import admin

from .models import Section, Post, Thread, User
# Register your models here.

admin.site.register(Section)
admin.site.register(Post)
admin.site.register(Thread)
admin.site.register(User)
