from django.contrib import admin 
from workArounds.models import Workday, MonthlyReport

admin.site.register(MonthlyReport)
admin.site.register(Workday)

# class WorkdayInline(admin.StackedInline):
#     model = Workday
#     extra = 30

# class MonthlyReportAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None,               {'fields': ['pub_date']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]
#     inlines = [WorkdayInline]

# admin.site.register(MonthlyReport, MonthlyReportAdmin)
# Register your models here.
