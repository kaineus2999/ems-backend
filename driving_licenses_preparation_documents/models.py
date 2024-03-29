from django.db import models
from common.models import CommonModel
from datetime import date

class Driving_licenses_preparation_document(CommonModel):

    name = models.CharField(
        max_length=180,
        default="",
    )

    expat = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="driving_licenses_preparation_documents",
    )

    is_english_driving_license = models.BooleanField(default=False)

    class KrbacktypeChoices(models.TextChoices):
        DRIVERS_LICENSE_TEST_ADMINISTRATION = ("drivers_license_test_administration", "운전면허시험관리단")
        ROAD_TRAFFIC_AUTHORITY = ("road_traffic_authority", "도로교통공단")
        
    krbacktype = models.CharField(
        max_length=50,
        choices=KrbacktypeChoices.choices,
        blank=True,)

    class TrbacktypeChoices(models.TextChoices):
        DRIVERS_LICENSE_TEST_ADMINISTRATION = ("drivers_license_test_administration", "Ehliyet Sinavi Yönetim Kurulu")
        ROAD_TRAFFIC_AUTHORITY = ("road_traffic_authority", "Trafik ve Karayollari Müdürlüğü")
        
    trbacktype = models.CharField(
        max_length=50,
        choices=TrbacktypeChoices.choices,
        blank=True,)

    class TypeChoices(models.TextChoices):
        TYPEONE = ("type_one", "Type one")
        TYPETWO = ("type_two", "Type two")
        
    type = models.CharField(
        max_length=10,
        choices=TypeChoices.choices,
        blank=True,)

    changed_address = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    changed_date = models.DateField(("When did you change address?"), default=date.today, blank=True,)


    two_changed_address = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    two_changed_date = models.DateField(("When did you change address?"), default=date.today, blank=True,)


    three_changed_address = models.CharField(
        max_length=180,
        default="",
        blank=True,
    )

    three_changed_date = models.DateField(("When did you change address?"), default=date.today, blank=True,)


    driving_license_number = models.CharField(
        max_length=180,
        default="",
    )

    driving_license_type = models.CharField(
        max_length=180,
        default="",
    )

    name_surname = models.CharField(
        max_length=180,
        default="",
    )

    id_number = models.CharField(
        max_length=180,
        default="",
    )

    house_address = models.CharField(
        max_length=700,
        default="",
        blank=True,
    )

    typeone_renewal_date = models.DateField(("Type one renewal date"), default=date.today, blank=True,)
    typetwo_renewal_date = models.DateField(("Type two renewal date"), default=date.today, blank=True,)

    issued_date = models.DateField(("Issued date"), default=date.today)
    
    issued_place = models.CharField(
        max_length=180,
        default="",
    )

    def __str__(self):
        return "Driving license preparation document"
    
    class Meta:
        verbose_name_plural = "Driving license preparation documents"