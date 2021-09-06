from django.db import models

# Create your models here.

class GovTable(models.Model):
    Name = models.TextField()
    Address = models.TextField()
    ZipCode = models.TextField()
    Email = models.TextField()

    def _str_(self):
        return self.Name