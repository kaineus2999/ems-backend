from django.db import models
from common.models import CommonModel
from datetime import date

class Announcement(CommonModel):

    title = models.CharField(
        max_length=180,
        default="",
    )

    subtitle = models.CharField(
        max_length=180,
        default="",
    )

    contents = models.CharField(
        max_length=180,
        default="",
    )

    detailed_information = models.CharField(
        max_length=180,
        default="",
    )

    responsible_person = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="announcements",
        default="",
    )

    class SubjectChoices(models.TextChoices):
        WORK_PERMITS = ("work_permits", "Work permits")
        REAL_ESTATE_AGENTS = ("real_estate_agents", "Real estate agents")
        MOVING_COMPANIES = ("moving_companies", "Moving companies")
        MOVING = ("moving", "Moving")
        HOUSES = ("houses", "Houses")
        GREEN_CARDS = ("green_cards", "Green cards")
        FAMILY_RESIDENCE_PERMITS = ("family_residence_permtis", "Family residence permits")
        DRIVING_LICENSES = ("driving_licenses", "Driving licenses")
        COMPANY_CARS = ("company_cars", "Company cars")

    subject = models.CharField(
        max_length=30,
        choices=SubjectChoices.choices,
        blank=True,)


    start_date = models.DateField(("Start date?"), default=date.today)
    start_time = models.TimeField(("Start time"), default="19:00")

    finish_date = models.DateField(("Finish date"), default=date.today)
    finish_time = models.TimeField(("Finish time"), default="19:00")


    def __str__(self):
        return "Announcement"
    
    class Meta:
        verbose_name_plural = "Announcements"