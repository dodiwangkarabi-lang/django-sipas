from django.shortcuts import render

from core.tables import build_table_context 

# selectors
from academics.siswa.selectors.selectors import (
    get_siswa
)

def get_siswa_list_view(request):
    init = request.GET.get("init")
    
    qs = get_siswa()
    
    columns = [
        {"key": "id", "label": "ID"},
    ]
    
    actions = [
        {
            "key": "detail",
            "label": "Detail",
            "url": "",
            "params": "id"
        }
    ]
    
    filter = {
        "tanggal": "created_at__date",
    }
    
    context = build_table_context(
        request=request,
        actions=actions,
        columns=columns,
        filters=filter,
        queryset=qs,
        search_fields=["judul"]
    )
    
    template = (
        "core/components/table/table.html"
        if init
        else "core/components/table/_table.html"
    )

    return render(request, template, context)