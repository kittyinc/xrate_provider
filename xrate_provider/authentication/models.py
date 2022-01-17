from os import urandom
from binascii import hexlify
from uuid import uuid4

from django.contrib.auth.models import AbstractBaseUser
from django.utils.translation import gettext as _
from django.db import models



def make_client_token():
    return hexlify(urandom(20)).decode()

class XrateApiUser(AbstractBaseUser):

    user_id = models.UUIDField(
        unique=True,
        default=uuid4,
        blank=False,
        null=False,
        verbose_name=_("user id"),
    )

    user_name = models.CharField(
        max_length=100,
        blank=False,
        null=False,
        verbose_name=_("user name"),
    )

    is_active = models.BooleanField(
        default=True,
    )
    password = None,
    last_login = None

    USERNAME_FIELD = 'user_id'


    def __str__(self):
        return "{}".format(self.user_name)





class APIToken(models.Model):
    """API client token."""
    key = models.CharField(
        max_length=40,
        primary_key=True,
        verbose_name=_('token'),
        default=make_client_token
        )

    user = models.ForeignKey(
        XrateApiUser, 
        related_name='token',
        on_delete=models.CASCADE,
        verbose_name=_('user'))
    
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name=_('issue date')
        )



    def save(self, *args, **kwargs):
        if not self.key:
            self.key = self.make_client_token()

        super().save(*args, **kwargs)

    class Meta:
        verbose_name = _('API token')
        verbose_name_plural = _('API tokens')

    def __str__(self):
        return "{} - {}".format(self.user, self.pub_date)
