from django.db import models

from datetime import timedelta, date
import hashlib


class Invitation(models.Model):
    """
    Invitation Model
    """

    id = models.AutoField(primary_key=True)
    telegram_id = models.CharField(max_length=15, unique=True)
    token = models.CharField(max_length=64, unique=True, blank=True, null=True)
    expiration_date = models.DateField()

    def save(self, *args, **kwargs):
        self.token = self.generate_token()
        self.expiration_date = date.today() + timedelta(days=2)
        super().save(*args, **kwargs)

    def generate_token(self):
        data = str(self.telegram_id).encode("utf-8")
        return hashlib.sha256(data).hexdigest()

    def __str__(self):
        return f'{self.telegram_id}'
