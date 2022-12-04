from django.db import models
from django.utils import timezone


class Blog(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=2550000)
    time = models.DateTimeField(auto_now=False, default=timezone.now)


def __str__(self):
    return self.title
