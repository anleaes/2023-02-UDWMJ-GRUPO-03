from django.db import models
from professionals.models import Professional

# Create your models here.

class Healthcenter(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    name = models.CharField('Nome', max_length=100)
    address = models.CharField('Endereco', max_length=200)   
    phone = models.CharField('Telefone celular', max_length=20)
    professional = models.ManyToManyField(Professional, through='HealthcenterProfessional', blank=True)
    
    class Meta:
        verbose_name = 'Healthcenter'
        verbose_name_plural = 'Healthcenters'
        ordering =['id']

    def __str__(self):
        return self.name


class HealthcenterProfessional(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    healthcenter = models.ForeignKey(Healthcenter, on_delete=models.CASCADE)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Profissional do Centro de Saude'
        verbose_name_plural = 'Profissionais do Centro de Saude'
        ordering =['id']

    def __str__(self):
        return self.professional.first_name