from django.contrib import admin
from .models import Story
import csv
from django.http import HttpResponse


@admin.register(Story)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ("date", "overall", "health", "love", "work", "favorite_story", "user_email")
    search_fields = ("date", "user__email")
    list_filter = ("date", "overall", "health", "love", "work", "favorite_story", "user__email")

    def user_email(self, obj):
        return obj.user.email







