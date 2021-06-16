from django.db import models

# Create your models here.

class Guide(models.Model):
    class Meta:
        db_table = 'guides'

    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    alt_description = models.CharField(max_length=300)
    audio_description = models.FileField()

    def __str__(self):
        return self.name