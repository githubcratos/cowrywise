# models.py
from django.db import models

class MyUuid(models.Model):
    uuid = models.CharField(max_length=35)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.uuid