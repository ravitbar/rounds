from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

def default_time(hour):
    now = datetime.now()
    start = now.replace(hour=hour, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)  

class WorkDay(models.Model):
    day    = models.ForeignKey('')
    worker = models.ForeignKey('auth.User')
    start  = models.DateTimeField(default = default_time(10))
    end    = models.DateTimeField(default = default_time(19))

class MonthlyReport(models.Model):
    month  = models.ForeignKey('')
    worker = models.ForeignKey('auth.User')
    total  = models.IntField()
    approvedDate = models.DateTimeField(blank=True, null=True)

    def approved(self):
        self.published_date = timezone.now()
        self.save()


