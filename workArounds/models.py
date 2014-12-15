from django.db import models
from django.utils import timezone
from datetime import datetime


# Create your models here.

def default_time(hour):
    now = datetime.now()
    start = now.replace(hour=hour, minute=0, second=0, microsecond=0)
    return start if start > now else start + timedelta(days=1)

class Worker(models.Model):
    worker = models.ForeignKey('auth.User')
    name   = models.CharField(max_length=200)

    def setCalendar(currentMonth):

    def getCalendar(currentMonth):

class WorkDay(models.Model):
    day    = models.DateField()
    worker = models.ForeignKey('auth.User')
    start  = models.DateTimeField()
    end    = models.DateTimeField()

class MonthlyReport(models.Model):
    month  = models.DateField()
    worker = models.ForeignKey('auth.User')
    total  = models.IntField()
    approvedDate = models.DateTimeField(blank=True, null=True)

    def approved(self):
        self.published_date = timezone.now()
        self.save()


