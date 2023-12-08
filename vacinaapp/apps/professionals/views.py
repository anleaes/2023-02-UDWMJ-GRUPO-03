from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProfessionalForm
from .models import Professional
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_professional(request):
    template_name = 'professionals/add_professional.html'
    context = {}
    if request.method == 'POST':
        form = ProfessionalForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('professionals:list_professionals')
    form = ProfessionalForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_professionals(request):
    template_name = 'professionals/list_professionals.html'
    professionals = Professional.objects.filter()
    context = {
        'professionals': professionals,
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_professional(request, id_professional):
    template_name = 'professionals/add_professional.html'
    context ={}
    professional = get_object_or_404(Professional, id=id_professional)
    if request.method == 'POST':
        form = ProfessionalForm(request.POST, instance=professional)
        if form.is_valid():
            form.save()
            return redirect('professionals:list_professionals')
    form = ProfessionalForm(instance=professional)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_professional(request, id_professional):
    professional = Professional.objects.get(id=id_professional)
    professional.delete()
    return redirect('professionals:list_professionals')