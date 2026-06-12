from predictions.models import TrainingRun

class TrainingRunRepository:
    def __init__(self):
        self.model = TrainingRun
    
    def create(self, **kwargs):
        self.model.objects.create(**kwargs)
        
        return self.model
    
    def update(self, id, **kwargs):
        return self.model.objects.filter(id=id).update(**kwargs)
    
    def update_or_create(self, dataset_version_obj, **kwargs):
        return self.model.objects.update_or_create(
            dataset_version=dataset_version_obj,
            defaults=kwargs # dict
        )
    
        
    