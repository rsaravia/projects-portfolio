from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=70)
    description = models.TextField()
    budget = models.DecimalField(max_digits=10,
                                 decimal_places=2)
    
    def __str__(self):
        return self.name

# Create your models here.
