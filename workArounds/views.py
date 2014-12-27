from django.shortcuts import render
from .models import MonthlyReport
from .models import Workday

# Create your views here.

def monthly_view(request):
    workdays = Workday.objects.filter()
    user     = request.user
    return render(request, 'workArounds/monthly_view.html', {'workdays': workdays, 'user': user})