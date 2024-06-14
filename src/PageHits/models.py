from django.db import models

# Create your models here.


class PageHits(models.Model):
    page = models.CharField(max_length=255, blank=True, null=True)
    hits = models.IntegerField(default=1)
    timestamp = models.DateTimeField(auto_now_add=True)
