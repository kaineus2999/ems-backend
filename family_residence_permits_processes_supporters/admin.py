from django.contrib import admin
from .models import Family_residence_permits_processes_supporter

@admin.register(Family_residence_permits_processes_supporter)
class Family_residence_permits_processes_supporterAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "responsible_person",
        "created_at",
    )

    list_filter = (
        "title",
        "responsible_person",
    )
    search_fields = (
        "title",
        "responsible_person",
    )