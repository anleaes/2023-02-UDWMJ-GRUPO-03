from django.db import models
from vaccines.models import Vaccine
from patients.models import Patient
from healthcenters.models import Healthcenter

# Create your models here.
class Appointment(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    registry_id = models.CharField('Numero de Registro', max_length=10, blank=True)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    health_center = models.ForeignKey(Healthcenter, on_delete=models.CASCADE)
    appointment_vaccine = models.ManyToManyField(Vaccine, through='AppointmentVaccine', blank=True)
    
    class Meta:
        verbose_name = 'Agendamento'
        verbose_name_plural = 'Agendamentos'
        ordering =['-created_on']

    def __str__(self):
        return self.registry_id


class AppointmentVaccine(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField('Quantidade',null=True, blank=True,default=0)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    vaccine = models.ForeignKey(Vaccine, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Vacina Agendada'
        verbose_name_plural = 'Vacinas Agendadas'
        ordering =['id']

    def __str__(self):
        return self.vaccine.name