from django.shortcuts import render

def index(request):
    return "oke"

from django.shortcuts import render

from core.tables import TableBuilder

# selectors
# from academics.selectors.selectors import get_all_siswa
from academics.siswa.selectors.selectors import get_all_siswa

# services
from core.utils.permissions import (
    has_group, is_admin, is_guru
)

def siswa_list_view(request):

    siswa_list = get_all_siswa()

    table = TableBuilder(
        headers=[
            "No",
            "Nama",
            "NIS",
            "Kelas",
            "Aksi",
        ]
    )

    for index, siswa in enumerate(siswa_list, start=1):

        actions = []

        # ADMIN
        if request.user.is_superuser:

            actions.append({
                "label": "Edit",
                "url": f"/siswa/{siswa.id}/edit/",
                "color": "blue"
            })

            actions.append({
                "label": "Delete",
                "url": f"/siswa/{siswa.id}/delete/",
                "color": "red"
            })

        # DOSEN
        elif request.user.groups.filter(name="Dosen").exists():

            actions.append({
                "label": "Detail",
                "url": f"/siswa/{siswa.id}/",
                "color": "green"
            })

        table.add_row(
            cells=[
                index,
                siswa.nama,
                siswa.nis,
                siswa.kelas,
            ],
            actions=actions
        )

    context = {
        "title": "Data Siswa",
        **table.to_dict()
    }

    return render(
        request,
        "students/siswa_list.html",
        context
    )
