from django.contrib import admin
from .models import Story, TodoItem


@admin.register(Story)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ("date", "overall", "health", "love", "work", "favorite_story", "user_email")
    search_fields = ("date", "user__email")
    list_filter = ("date", "overall", "health", "love", "work", "favorite_story", "user__email")

    def user_email(self, obj):
        return obj.user.email

@admin.register(TodoItem)
class StoriesAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "completed", "user_email")
    search_fields = ("title", "category", "completed",  "user__email")
    list_filter = ("title", "category", "completed",  "user__email")

    def user_email(self, obj):
        return obj.user.email









