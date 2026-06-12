from django.shortcuts import render, redirect, get_object_or_404

# tables
from academics.siswa.web.tables import (
    SiswaTable, KehadiranTable
)

# models
from academics.models import Siswa

# forms
from academics.web.siswa.forms import (
    SiswaForm
)
from academics.kehadiran.web.forms import KehadiranForm
from academics.akademik.web.forms import DataAkademikForm

# selectors
# from academics.selectors.selectors import (
#     get_all_siswa
# )

from academics.siswa.selectors.selectors import (
    get_all_siswa, get_siswa_by_id
)

# services
from academics.services.services import SiswaService

# message
from core.messages import (
    show_success,
    show_error,
    show_form_errors
)

def index(request):
    siswa_list = get_all_siswa()
    siswa_table = SiswaTable()
    siswa_table.build_rows(siswa_list)
    
    form = SiswaForm(request.POST or None)
    
    if request.method == "POST":
        if not form.is_valid():
            show_form_errors(request, form)
            return redirect("academics:siswa:siswa_web:index")
        
        siswa_service = SiswaService()
        siswa_service.create(**form.cleaned_data)
        
        show_success(request, "Siswa berhasil ditambahkan")
        
        return redirect("academics:siswa:siswa_web:index")
    
    context = {
        **siswa_table.to_dict(),
        "form": form
    }
    return render(request, "academics/siswa/pages/index.html", context)

def siswa_delete_view(request, siswa_id):
    siswa_service = SiswaService()
    siswa_service.delete(siswa_id)
    
    show_success(request, "Siswa berhasil dihapus")
    
    return redirect("academics:siswa:siswa_web:index")

def siswa_detail_view(request, siswa_id):
    siswa = get_object_or_404(Siswa, id=siswa_id)

    form = SiswaForm(request.POST or None, instance=siswa)
    kehadiran_form = KehadiranForm(request.POST or None)
    akademik_form = DataAkademikForm(request.POST or None)
    
    if siswa.has_kehadiran:
        kehadiran_form = KehadiranForm(request.POST or None, instance=siswa.kehadiran)
        
    if siswa.has_data_akademik:
        akademik_form = DataAkademikForm(request.POST or None, instance=siswa.data_akademik)
    
    if request.method == "POST":
        if not form.is_valid():
            show_form_errors(request, form)
            return redirect("academics:siswa:siswa_web:detail", siswa_id=siswa_id)
        
        siswa_service = SiswaService()
        siswa_service.update(siswa_id, **form.cleaned_data)
        
        show_success(request, "Siswa berhasil diupdate")
        
        return redirect("academics:siswa:siswa_web:detail", siswa_id=siswa_id)
    
    context = {
        "siswa": siswa,
        "form": form,
        "kehadiran_form": kehadiran_form,
        "akademik_form": akademik_form
    }
    return render(request, "academics/siswa/pages/detail.html", context)

def siswa_list_view(request):
    siswa_list = get_all_siswa()
    siswa_table = SiswaTable()
    siswa_table.build_rows(siswa_list)
    
    form = SiswaForm(request.POST or None)
    
    if request.method == "POST":
        if not form.is_valid():
            show_form_errors(request, form)
            return redirect("academics:siswa:siswa_web:list")
        
        siswa_service = SiswaService()
        siswa_service.create(**form.cleaned_data)
        
        show_success(request, "Siswa berhasil ditambahkan")
        
        return redirect("academics:siswa:siswa_web:list")
    
    context = {
        **siswa_table.to_dict(),
        "form": form
    }
    return render(request, "academics/siswa/pages/list.html", context)