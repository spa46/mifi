from django.db import models


class FIndex(models.Model):
    code = models.CharField(max_length=32)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=256)
