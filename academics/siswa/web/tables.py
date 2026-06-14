from core.tables import TableBuilder
from django.urls import reverse, reverse_lazy

class KehadiranTable(TableBuilder):
    table_title = "Kehadiran"

class SiswaTable(TableBuilder):
    table_title = "Siswa"

    headers = [
        "No",
        "NIS",
        "Nama",
        "Prediksi Prestasi",
        "Aksi",
    ]

    def build_rows(self, queryset):
        """
        membuat tabel

        Args:
            queryset (queryset): list_object siswa
            
        Example:
            table = SiswaTable()
            table.build_rows(get_all_siswa())
        """

    

        for index, siswa in enumerate(queryset, start=1):

            self.add_row(
                cells=[
                    index,
                    siswa.nis,
                    siswa.nama,
                    siswa.hasil_prediksi
                ],
                actions=[
                    # {
                    #     "label": "Edit",
                    #     "url": f"/siswa/{siswa.id}/edit/",
                    #     "color": "blue",
                    #     "action_type": "edit"
                    # },
                    {
                        "label": "Delete",
                        "url": f"{reverse('academics:siswa:siswa_web:delete', args=[siswa.id])}",
                        "color": "red",
                        "action_type": "delete"
                    },
                    {
                        "label": "Detail",
                        "url": f"{reverse('academics:siswa:siswa_web:detail', args=[siswa.id])}",
                        "color": "green",
                        "action_type": "detail"
                    }
                ]
            )