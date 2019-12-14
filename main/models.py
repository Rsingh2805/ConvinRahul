from django.db import models
from model_utils import FieldTracker


class DataModel(models.Model):
    tracker = FieldTracker()
    file = models.FileField(upload_to="uploads/", verbose_name="File field")
    encrypted = models.CharField(max_length=64, verbose_name="Encrypted Value")

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


