from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# services
from core.services.dashboard_service import StatistikService

@login_required(login_url="accounts:login")
def index(request):
    context = {
        "statistik_siswa": StatistikService().statistik_siswa(),
    }
    return render(request, "core/dashboard/dashboard.html", context)
