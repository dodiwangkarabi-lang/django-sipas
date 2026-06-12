from django.shortcuts import render
from django.http import HttpResponse

# service
from academics.services.services import (
    DataAkademikServices
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
from academics.akademik.web.forms import DataAkademikForm

# selectors
from academics.siswa.selectors.selectors import (
    get_siswa_by_id
)

def index(request):
    return render(request, "academics/kehadiran/pages/index.html")

def create(request, siswa_id):
    siswa = get_siswa_by_id(siswa_id)
    form = DataAkademikForm(request.POST or None)
    
    if request.method == "POST":
        if not form.is_valid():
            show_form_errors(request, form)
            
            return redirect_back(request)

        data = form.cleaned_data.copy()
        data["siswa"] = siswa
        akademik_service = DataAkademikServices()
        akademik_service.create(**data)
        show_success(request, "data akademik berhasil ditambahkan")
        
        return redirect_back(request)
    
    return render(request, "academics/akademik/pages/create.html")

def detail(request, id):
    form = DataAkademikForm(request.POST or None)
    
    if request.method == "POST":
        if not form.is_valid():
            show_form_errors(request, form)
            
            return redirect_back(request)

        data = form.cleaned_data
        akademik_service = DataAkademikServices()
        akademik_service.update(id, **data)
        show_success(request, "data akademik berhasil diupdate")
        
        return redirect_back(request)
    
    return render(request, "academics/akademik/pages/detail.html")