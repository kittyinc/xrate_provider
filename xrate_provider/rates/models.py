from django.db import models
from django.utils.translation import gettext as _
from uuid import uuid4

PROVIDER_CHOICES = (
    ("DOF", "Diaro Oficial de la Federación"),
    ("FXR", "Fixer"),
    ("BXO", "Banxico"),
)

class Rate(models.Model):

    rate_id = models.UUIDField(
        primary_key=True,
        default=uuid4,
        blank=False,
        null=False,
        verbose_name=_("rate id"),
    )

    provider = models.CharField(
        max_length=3,
        choices=PROVIDER_CHOICES,
        null=False,
        blank=False,
        verbose_name=_("provider"),

    )

    last_updated = models.DateTimeField(
        auto_now_add=True,
        null=False,
        blank=False,
        verbose_name=_("last updated"),

    )

    last_updated_provider = models.DateTimeField(
        null=False,
        blank=False,
        verbose_name=_("last updated by provider"),
    )

    value = models.DecimalField(
        max_digits=20, # what happens if the value fluctuates wildly overnight i.e 1 USD = 10,500 MXN.
        decimal_places=6,
        null=False,
        blank=False,
        verbose_name=_("value"),

    )

    variant = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    variant_name = models.CharField(
        max_length=25,
        null=False,
        blank=False,
        default="default", 
    )

    def __str__(self):
        return "{} - {}: {}".format(self.provider, self.variant, self.value)

    class Meta:
        pass