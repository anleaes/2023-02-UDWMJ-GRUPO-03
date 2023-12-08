from django.shortcuts import render, get_object_or_404, redirect
from .forms import AppointmentForm, AppointmentVaccineForm
from .models import Appointment, AppointmentVaccine, Vaccine, Patient

# Create your views here.
def add_appointment(request, id_patient):
    template_name = 'appointments/add_appointment.html'
    context = {}
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        print(form)
        if form.is_valid():
            f = form.save(commit=False)
            print("aaaaa")
            f.patient = Patient.objects.get(id=id_patient)
            f.save()
            form.save_m2m()
            return redirect('appointments:list_appointments')
    form = AppointmentForm()
    context['form'] = form
    return render(request, template_name, context)

def list_appointments(request):
    template_name = 'appointments/list_appointments.html'
    appointments = Appointment.objects.filter()
    appointment_vaccines = AppointmentVaccine.objects.filter()
    vaccines = Vaccine.objects.filter()
    patients = Patient.objects.filter()
    context = {
        'appointments': appointments,
        'appointment_vaccines': appointment_vaccines,
        'vaccines': vaccines,
        'patients': patients
    }
    return render(request, template_name, context)

def delete_appointment(request, id_appointment):
    appointment = Appointment.objects.get(id=id_appointment)
    appointment.delete()
    return redirect('appointments:list_appointments')

def add_appointment_vaccine(request, id_appointment):
    template_name = 'appointments/add_appointment_vaccine.html'
    context = {}
    if request.method == 'POST':
        form = AppointmentVaccineForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.appointment = Appointment.objects.get(id=id_appointment)
            f.save()
            form.save_m2m()
            return redirect('appointments:list_appointments')
    form = AppointmentVaccineForm()
    context['form'] = form
    return render(request, template_name, context)

def delete_appointment_vaccine(request, id_appointment_vaccine):
    appointment_vaccine = AppointmentVaccine.objects.get(id=id_appointment_vaccine)
    appointment_vaccine.delete()
    return redirect('appointments:list_appointments')