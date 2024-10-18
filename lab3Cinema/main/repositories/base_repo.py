from django.db import models

class BaseRepo:
    def __init__(self, model: models.Model):
        self.model = model

    def getAll(self):
        return self.model.objects.all()

    def getById(self, id):
        try:
            return self.model.objects.get(id=id)
        except self.model.DoesNotExist:
            return None

    def create(self, **data):
        return self.model.objects.create(**data)

    def deleteObj(self, id):
        to_delete = self.getById(id)
        if to_delete:
            return to_delete.delete()
        return None