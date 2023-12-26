from django.db import models
from time import timezone
from datetime import timedelta


class Invitation(models.Model):
    """
    Invitation Model
    """
    id = models.AutoField(primary_key=True)
    telegram_id = models.CharField(max_length=10, unique=True)
    expiration_date = models.DateField(default=timezone.now + timedelta(days=2))


