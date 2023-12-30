from django.db import models
from datetime import timedelta, date
import hashlib


class Invitation(models.Model):
    """
    Invitation Model
    """
    def generate_token(self):
        data = self.telegram_id.encode("utf-8")
        return hashlib.sha256(data).hexdigest()

    id = models.AutoField(primary_key=True)
    telegram_id = models.CharField(max_length=9, unique=True)
    token = models.CharField(max_length=64, unique=True, default=generate_token)
    expiration_date = models.DateField(default=date.today() + timedelta(days=2))


