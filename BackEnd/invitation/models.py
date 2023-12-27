from django.db import models
from datetime import timedelta, date


class Invitation(models.Model):
    """
    Invitation Model
    """
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, blank=True, default='Someone')
    telegram_id = models.CharField(max_length=9, unique=True)
    token = models.CharField(max_length=64, unique=True)
    expiration_date = models.DateField(default=date.today() + timedelta(days=2))
