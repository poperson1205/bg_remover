from django.db import models

# Create your models here.
class ImageFileModel(models.Model):
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.image.name