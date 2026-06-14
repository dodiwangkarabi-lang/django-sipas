from django.db import models

from django.core.files.storage import FileSystemStorage
from django.conf import settings

dataset_storage = FileSystemStorage(
    location=settings.DATASET_STORAGE_DIR,
    base_url="/predictions/datasets/"
)

model_storage = FileSystemStorage(
    location=settings.MODEL_STORAGE_DIR,
    base_url="/predictions/ml_models/"
)

class Dataset(models.Model):
    class DatasetType(models.TextChoices):
        CSV = "csv", "CSV"
        PARQUET = "parquet", "Parquet"
        JSON = "json", "JSON"

    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)

    dataset_type = models.CharField(
        max_length=20,
        choices=DatasetType.choices,
        default=DatasetType.CSV
    )

    # versi aktif (pointer ke DatasetVersion)
    active_version = models.ForeignKey(
        "DatasetVersion",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="+"
    )

    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.pk} - {self.name}"
    
class DatasetVersion(models.Model):
    dataset = models.ForeignKey(
        "Dataset",
        on_delete=models.CASCADE,
        related_name="versions"
    )

    version = models.CharField(max_length=50)
    file = models.FileField(upload_to="", storage=dataset_storage, null=True, blank=True)

    row_count = models.PositiveIntegerField(default=0)
    column_count = models.PositiveIntegerField(default=0)

    file_size = models.BigIntegerField(null=True, blank=True)
    checksum = models.CharField(max_length=128, blank=True, null=True, unique=True)

    schema = models.JSONField(blank=True, null=True)
    preview = models.JSONField(blank=True, null=True)
    columns = models.JSONField(null=True, blank=True)
    features = models.JSONField(null=True, blank=True)
    target = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
        constraints = [
            models.UniqueConstraint(
                fields=["dataset", "version"],
                name="unique_dataset_version"
            )
        ]

    def __str__(self):
        return f"{self.dataset.name} - {self.version}"
    
class DatasetUsage(models.Model):
    dataset_version = models.ForeignKey(
        "DatasetVersion",
        on_delete=models.CASCADE,
        related_name="usages"
    )

    model_name = models.CharField(max_length=255)
    model_version = models.CharField(max_length=50, blank=True, null=True)

    metrics = models.JSONField(blank=True, null=True)
    parameters = models.JSONField(blank=True, null=True)

    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(blank=True, null=True)

    duration_seconds = models.FloatField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ["-started_at"]

    def __str__(self):
        dataset_name = getattr(self.dataset_version.dataset, "name", "unknown")
        return f"{self.model_name} - {dataset_name}"

class HasilTraining(models.Model):
    nama_model = models.CharField(max_length=100)
    akurasi = models.FloatField()
    lokasi_model = models.CharField(max_length=255)

    def __str__(self):
        return self.nama_model
    
class HasilPrediksi(models.Model):
    hasil = models.CharField(max_length=100)

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.hasil
    
class TrainingRun(models.Model):
    dataset_version = models.ForeignKey("DatasetVersion", on_delete=models.CASCADE)

    algorithm = models.CharField(max_length=100)
    hyperparameters = models.JSONField(null=True, blank=True)

    metrics = models.JSONField(null=True, blank=True)
    
    dataset_metadata = models.JSONField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.pk} - {self.algorithm}"
    
class ModelML(models.Model):
    training_run = models.ForeignKey("TrainingRun", on_delete=models.CASCADE, null=True, blank=True)

    nama = models.CharField(max_length=100, unique=True)

    file_model = models.FileField(
        upload_to="",
        storage=model_storage,
        help_text="File model hasil training (pickle/joblib/onnx)",
        blank=True,
        null=True
    )
    
    checksum = models.CharField(max_length=64, unique=True, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.nama