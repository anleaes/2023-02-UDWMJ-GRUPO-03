from django.db import models
from batches.models import Batch

# Create your models here.

class Vaccine(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=50)
    target_disease = models.TextField('Doenca Alvo', max_length=100)
    Batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Vaccine'
        verbose_name_plural = 'Vaccines'
        ordering =['id']

    def __str__(self):
        return self.name