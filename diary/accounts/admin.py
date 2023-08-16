from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from diary.stories.models import Story

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(UserAdmin):
    list_display = ("email", "first_name", "last_name", "is_staff", "story_count")
    search_fields = ("email", "first_name", "last_name")
    ordering = ("email", "first_name", "last_name", "is_staff",)
    list_filter = ("is_staff", )
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        (_("Personal info"), {"fields": ("first_name", "last_name")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )

    def story_count(self, obj):
        return Story.objects.filter(user_id=obj.id).count()

