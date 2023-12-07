from django.shortcuts import render, get_object_or_404, redirect
from .forms import VaccineForm
from .models import Vaccine

# Create your views here.

def add_product(request):
    template_name = 'vaccines/add_product.html'
    context = {}
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('vaccines:list_vaccines')
    form = VaccineForm()
    context['form'] = form
    return render(request, template_name, context)

def list_vaccines(request):
    template_name = 'vaccines/list_vaccines.html'
    vaccines = Vaccine.objects.filter()
    context = {
        'vaccines': vaccines
    }
    return render(request, template_name, context)

def edit_product(request, id_product):
    template_name = 'vaccines/add_product.html'
    context ={}
    product = get_object_or_404(Vaccine, id=id_product)
    if request.method == 'POST':
        form = VaccineForm(request.POST, request.FILES,  instance=product)
        if form.is_valid():
            form.save()
            return redirect('vaccines:list_vaccines')
    form = VaccineForm(instance=product)
    context['form'] = form
    return render(request, template_name, context)

def delete_product(request, id_product):
    product = Vaccine.objects.get(id=id_product)
    product.delete()
    return redirect('vaccines:list_vaccines')