import django_filters
from django.db.models import F, FloatField, ExpressionWrapper, Sum
from django.db.models.functions import Cast
from rest_framework import routers, viewsets
from app.models import MetricModel
from app.serializers import MetricSerializer
from app.utils import Round2decimals


class MetricFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter('date', lookup_expr='gte')
    date_to = django_filters.DateFilter('date', lookup_expr='lte')

    class Meta:
        model = MetricModel
        fields = (
            'date_from',
            'date_to',
            'channel',
            'country',
            'os'
        )


class MetricViewSet(viewsets.ModelViewSet):
    serializer_class = MetricSerializer
    queryset = MetricModel.objects.all()
    filterset_class = MetricFilter
    ordering_fields = '__all__'
    groupby_fields = (
        'date',
        'channel',
        'country',
        'os'
    )

    def get_queryset(self):
        if 'groupby' in self.request.query_params:
            groupby_fields = self.request.query_params.get('groupby').split(',')
            if all(i in self.groupby_fields for i in groupby_fields):
                return self.queryset.values(*groupby_fields).annotate(
                    impressions=Sum('impressions'),
                    clicks=Sum('clicks'),
                    installs=Sum('installs'),
                    spend=Sum('spend'),
                    revenue=Sum('revenue'),
                    cpi=Round2decimals(ExpressionWrapper((F('spend') * 1.0) / F('installs'), FloatField()))
                )
        return self.queryset.annotate(
            cpi=Round2decimals(ExpressionWrapper((F('spend') * 1.0) / F('installs'), FloatField()))
        )
