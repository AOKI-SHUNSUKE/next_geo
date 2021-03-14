from django.contrib import admin
from .models import Task,Post,Coordinate
# Register your models here.

admin.site.register(Post)
admin.site.register(Task)
admin.site.register(Coordinate)