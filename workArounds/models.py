from django.db import models as m
from django.utils import timezone
from datetime import datetime
import calendar


# Create your models here.

class MonthlyReport(m.Model):
    month  = m.DateField()
    worker = m.ForeignKey('auth.User')
    total  = m.IntegerField()
    approvedDate = m.DateTimeField(blank=True, null=True)

    # def __unicode__(self):
    #     return self.month

class Workday(m.Model):
    day    = m.DateField()
    worker = m.ForeignKey('auth.User')
    start  = m.DateTimeField(blank=True, null=True)
    end    = m.DateTimeField(blank=True, null=True)

    # def __unicode__(self):
    #     return '%s' % (self.worker.username)

    # def days_in_month(self, year, month):
    #     range = calendar.monthrange(year,month)
    #     return self.day >= datetime.date(year, month, range[0]) and self.day <= datetime.date(year, month, range[0])

