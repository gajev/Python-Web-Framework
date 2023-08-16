from django.contrib import admin
from .models import PartnerUser

# Register your models here.


@admin.register(PartnerUser)
class PartnerAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "type_partner")
    search_fields = ("email", "first_name", "last_name", "type_partner")
    list_filter = ("type_partner",)