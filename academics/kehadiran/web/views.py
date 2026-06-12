from django.shortcuts import render
from django.http import HttpResponse

# service
from academics.services.services import (
    KehadiranServices
)

# message
from core.messages import (
    show_success,
    show_error,
    show_form_errors
)

# utils
from core.utils.redirects import (
    redirect_back
)

# form
from academics.kehadiran.web.forms import KehadiranForm

# selectors
from academics.siswa.selectors.selectors import (
    get_siswa_by_id
)

def index(request):
    return render(request, "academics/kehadiran/pages/index.html")

def create(request, siswa_id):
    siswa = get_siswa_by_id(siswa_id)
    form = KehadiranForm(request.POST or None)
    
    if request.method == "POST":
        if not form.is_valid():
            show_form_errors(request, form)
            
            return redirect_back(request)

        data = form.cleaned_data.copy()
        data["siswa"] = siswa
        kehadiran_service = KehadiranServices()
        kehadiran_service.create(**data)
        show_success(request, "Kehadiran berhasil ditambahkan")
        
        return redirect_back(request)
    
    return render(request, "academics/kehadiran/pages/create.html")

def detail(request, kehadiran_id):
    form = KehadiranForm(request.POST or None)
    
    if request.method == "POST":
        if not form.is_valid():
            show_form_errors(request, form)
            
            return redirect_back(request)

        data = form.cleaned_data
        kehadiran_service = KehadiranServices()
        kehadiran_service.update(kehadiran_id, **data)
        show_success(request, "Kehadiran berhasil diupdate")
        
        return redirect_back(request)
    
    return render(request, "academics/kehadiran/pages/detail.html")