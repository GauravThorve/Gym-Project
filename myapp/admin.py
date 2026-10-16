from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(ContactModel)


from django.contrib import admin
from .models import Trainer

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "specialization",
        "experience",
        "is_active",
    )
    search_fields = ("name", "specialization")

    list_filter = ("is_active", "specialization")
