from django.db import models
from appointments.models import Appointment
from professionals.models import Professional

# Create your models here.
class VaccinationRegistry(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    date = models.DateField('Data da vacinacao', auto_now_add=False, auto_now=False)
    professional = models.ForeignKey(Professional, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = 'Registro de Vacinacao'
        verbose_name_plural = 'Registros de Vacinacao'
        ordering =['id']

    def __str__(self):
        return self.appointment.registry_id