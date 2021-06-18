from django.db import models

# Create your models here.

class Guide(models.Model):
    class Meta:
        db_table = 'guides'

    image = models.ImageField()
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    alt_description = models.CharField(max_length=300)
    audio_description_pt = models.FileField()
    audio_description_en = models.FileField()
    audio_description_es = models.FileField()

    def __str__(self):
        return self.name