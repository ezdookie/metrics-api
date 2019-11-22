import csv
from django.core.management.base import BaseCommand
from app.models import MetricModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('seeds/dataset.csv') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row['spend'] = float(row['spend'])
                row['revenue'] = float(row['revenue'])
                MetricModel.objects.create(**row)
        self.stdout.write(self.style.SUCCESS('Data successfully loaded...!'))
