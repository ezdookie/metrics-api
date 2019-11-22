from django.db import models


class MetricModel(models.Model):
    date = models.DateField(blank=True)
    channel = models.CharField(max_length=50, blank=True)
    country = models.CharField(max_length=2, blank=True)
    os = models.CharField(max_length=50, blank=True)
    impressions = models.IntegerField(blank=True)
    clicks = models.IntegerField(blank=True)
    installs = models.IntegerField(blank=True)
    spend = models.IntegerField(blank=True)
    revenue = models.IntegerField(blank=True)

    class Meta:
        db_table = 'metric'
