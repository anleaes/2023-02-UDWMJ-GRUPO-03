from django.shortcuts import render, get_object_or_404, redirect
from .forms import VaccinationRegistryForm
from .models import VaccinationRegistry

# Create your views here.
def add_vaccinationregistry(request):
    template_name = 'vaccinationregistries/add_vaccinationregistry.html'
    context = {}
    if request.method == 'POST':
        form = VaccinationRegistryForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('vaccinationregistries:list_vaccinationregistries')
    form = VaccinationRegistryForm()
    context['form'] = form
    return render(request, template_name, context)

def list_vaccinationregistries(request):
    template_name = 'vaccinationregistries/list_vaccinationregistries.html'
    vaccinationregistries = VaccinationRegistry.objects.filter()
    context = {
        'vaccinationregistries': vaccinationregistries
    }
    return render(request, template_name, context)

def edit_vaccinationregistry(request, id_vaccinationregistry):
    template_name = 'vaccinationregistries/add_vaccinationregistry.html'
    context ={}
    vaccinationregistry = get_object_or_404(VaccinationRegistry, id=id_vaccinationregistry)
    if request.method == 'POST':
        form = VaccinationRegistryForm(request.POST, request.FILES,  instance=vaccinationregistry)
        if form.is_valid():
            form.save()
            return redirect('vaccinationregistries:list_vaccinationregistries')
    form = VaccinationRegistryForm(instance=vaccinationregistry)
    context['form'] = form
    return render(request, template_name, context)

def delete_vaccinationregistry(request, id_vaccinationregistry):
    vaccinationregistry = VaccinationRegistry.objects.get(id=id_vaccinationregistry)
    vaccinationregistry.delete()
    return redirect('vaccinationregistries:list_vaccinationregistries')