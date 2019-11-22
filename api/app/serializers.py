from rest_framework import serializers
from app.models import MetricModel


class MetricSerializer(serializers.ModelSerializer):
    cpi = serializers.CharField(required=False)

    class Meta:
        model = MetricModel
        fields = [
            'date',
            'channel',
            'country',
            'os',
            'impressions',
            'clicks',
            'installs',
            'spend',
            'revenue',
            'cpi'
        ]
