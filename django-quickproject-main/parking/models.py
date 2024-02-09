from django.db import models

# Create your models here.

class Parking(models.Model):
    company = models.CharField(max_length=100)
    local = models.CharField(max_length=100)
    carCapacity = models.IntegerField(default=0)

    def __str__(self):
        return self.company