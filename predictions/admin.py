from django.contrib import admin

# models
from predictions.models import (
    HasilTraining, HasilPrediksi, ModelML,
    Dataset, DatasetUsage, DatasetVersion,
    TrainingRun
)

admin.site.register(ModelML)
admin.site.register(HasilPrediksi)
admin.site.register(HasilTraining)

admin.site.register(Dataset)
admin.site.register(DatasetUsage)
admin.site.register(DatasetVersion)

admin.site.register(TrainingRun)