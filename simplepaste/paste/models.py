from django.db import models

# Create your models here.
class PasteBox(models.Model):
    title = models.CharField(max_length=30)
    paste = models.CharField(max_length=2000)

    def __str__(self):
        return self.title
