from django.db import models
from brands.models import Brand

# Create your models here.

class Batch(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    number = models.CharField('Numero do Lote', max_length=7)
    date = models.DateField('Data de Fabricacao', auto_now=False, auto_now_add=False)
    expiration_date = models.DateField('Data Expiracao', auto_now=False, auto_now_add=False)
    quantity = models.IntegerField('Quantidade de Vacinas')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = 'Lote'
        verbose_name_plural = 'Lotes'
        ordering =['id']

    def __str__(self):
        return self.number