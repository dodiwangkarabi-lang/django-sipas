from rest_framework.routers import DefaultRouter

app_name = "academics_api"

router = DefaultRouter()

from academics.api.viewsets import (
    SiswaViewSet, DataAkademikViewSet, KehadiranViewSet, PrediksiPrestasiViewSet
)

router.register("siswa", SiswaViewSet, basename="siswa")
router.register("data-akademik", DataAkademikViewSet, basename="data-akademik")
router.register("kehadiran", KehadiranViewSet, basename="kehadiran")
router.register("prediksi-prestasi", PrediksiPrestasiViewSet, basename="prediksi-prestasi")

urlpatterns = router.urls