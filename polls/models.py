from django.db import models
from django.db.models.fields import IntegerField

# Create your models here.
class info(models.Model):
    name = models.TextField(blank=False)
    nationality = models.TextField(blank=False)
    reason = models.TextField(blank=False)
    year = IntegerField(blank=False)

    def __str__(self):
        return self.name
