from django.db import models

# Create your models here.

class Professional(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    first_name = models.CharField('Nome', max_length=50)
    last_name = models.CharField('Sobrenome', max_length=100)
    age = models.IntegerField('Idade')
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    )
    gender = models.CharField('Genero', max_length=1, choices=GENDER_CHOICES)
    cpf = models.CharField('CPF', max_length=11)
    phone = models.CharField('Telefone celular', max_length=20)
    address = models.CharField('Endereco', max_length=200)   
    license = models.CharField('Registro Profissional', max_length=50)
    health_plan = models.CharField('Plano de saude', max_length=50)
    
    class Meta:
        verbose_name = 'Professional'
        verbose_name_plural = 'Professionals'
        ordering =['id']

    def __str__(self):
        return self.first_name
