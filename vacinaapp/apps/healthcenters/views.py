from .forms import HealthcenterForm
from .models import Healthcenter, Professional, HealthcenterProfessional
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.

def add_healthcenter(request):
    template_name = 'healthcenters/add_healthcenter.html'
    context = {}
    if request.method == 'POST':
        form = HealthcenterForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('healthcenters:list_healthcenters')
    form = HealthcenterForm()
    context['form'] = form
    return render(request, template_name, context)

def list_healthcenters(request):
    template_name = 'healthcenters/list_healthcenters.html'
    healthcenter_professionals = HealthcenterProfessional.objects.filter()
    professionals = Professional.objects.filter()
    healthcenters = Healthcenter.objects.filter()
    context = {
        'healthcenters': healthcenters,
        'professionals': professionals,
        'healthcenter_professionals': healthcenter_professionals
    }
    return render(request, template_name, context)

def edit_healthcenter(request, id_healthcenter):
    template_name = 'healthcenters/add_healthcenter.html'
    context ={}
    healthcenter = get_object_or_404(Healthcenter, id=id_healthcenter)
    if request.method == 'POST':
        form = HealthcenterForm(request.POST, instance=healthcenter)
        if form.is_valid():
            form.save()
            return redirect('healthcenters:list_healthcenters')
    form = HealthcenterForm(instance=healthcenter)
    context['form'] = form
    return render(request, template_name, context)

def delete_healthcenter(request, id_healthcenter):
    healthcenter = Healthcenter.objects.get(id=id_healthcenter)
    healthcenter.delete()
    return redirect('healthcenters:list_healthcenters')
