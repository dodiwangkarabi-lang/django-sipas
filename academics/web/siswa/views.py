from django.shortcuts import render, redirect

# tables
from core.tables import TableBuilder, SiswaTable

# models
from academics.models import Siswa

# forms
from academics.web.siswa.forms import SiswaForm

# selectors
from academics.selectors.selectors import get_all_siswa

# services
from academics.services.services import SiswaService

# message
from core.messages import (
    show_success,
    show_error,
    show_form_errors
)

def siswa_list_view(request):
    siswa_list = get_all_siswa()
    siswa_table = SiswaTable()
    siswa_table.build_rows(siswa_list)
    
    form = SiswaForm(request.POST or None)
    
    if request.method == "POST":
        if not form.is_valid():
            show_form_errors(request, form)
            return redirect("academics:siswa:list")
        
        siswa_service = SiswaService()
        siswa_service.create(**form.cleaned_data)
        
        show_success(request, "Siswa berhasil ditambahkan")
        
        return redirect("academics:siswa:list")
    
    context = {
        **siswa_table.to_dict(),
        "form": form
    }
    return render(request, "academics/siswa/list.html", context)