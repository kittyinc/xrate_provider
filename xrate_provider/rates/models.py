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
        verbose_name=_("last_updated"),

    )

    value = models.DecimalField(
        max_digits=6,
        decimal_places=4,
        null=False,
        blank=False,
        verbose_name=_("value"),

    )

    variant = models.PositiveIntegerField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return "{} - {}: {}".format(self.provider, self.variant, self.value)

    class Meta:
        pass



# for every enumerator, get number of variants, assemble list or something
# for every variant get latest value
# assemble into serializer
# Output as view
