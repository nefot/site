from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=255)
    image = models.ImageField(upload_to='portfolio/images/')
    url = models.URLField(blank=True)
    time = models.DateTimeField(auto_now=False, default=timezone.now)


