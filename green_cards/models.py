from django.db import models
from common.models import CommonModel
from datetime import date

class Green_card(CommonModel):
    name = models.CharField(
        max_length=180,
        default="",
    )
    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="green_cards",
        default="",
    )
    green_card_expiry_date = models.DateField(
        null=True,
        blank=True,
    )
    overseas_car_insurance_expiry_date = models.DateField(
        null=True,
        blank=True,
    )
    
    def __str__(self):
        return "Green card"
    
    class Meta:
        verbose_name_plural = "Green cards"
    