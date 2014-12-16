from django.db import models as m
from django.utils import timezone
from datetime import datetime


# Create your models here.

class Worker(m.Model):
    worker   = m.ForeignKey('auth.User')
    name     = m.CharField(max_length=200)
    password = m.CharField(max_length=20)

    # def setCalendar(currentMonth):

    # def getCalendar(currentMonth):

    def get_absolute_url(self):
        return reverse('workArounds.views.calendar', args=[self.slug])

    def __init__(self, name, password):
        self.name     = name
        self.password = password
        self.save()


class WorkDay(m.Model):
    day    = m.DateField()
    worker = m.ForeignKey('auth.User')
    start  = m.DateTimeField(blank=True, null=True)
    end    = m.DateTimeField(blank=True, null=True)

class MonthlyReport(m.Model):
    month  = m.DateField()
    worker = m.ForeignKey('auth.User')
    total  = m.IntegerField()
    approvedDate = m.DateTimeField(blank=True, null=True)

    def approved(self):
        self.published_date = timezone.now()
        self.save()


