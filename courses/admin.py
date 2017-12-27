from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from .models import Course, Topic

class CourseInLine(admin.TabularInline):
    model=Course

class TopicAdmin(admin.ModelAdmin):
    inlines =[CourseInLine]

admin.site.register(Topic,TopicAdmin)
admin.site.register(Course)
