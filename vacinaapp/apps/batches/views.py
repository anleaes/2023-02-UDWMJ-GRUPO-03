from django.shortcuts import render, get_object_or_404, redirect
from .forms import BatchForm
from .models import Batch
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_batch(request):
    template_name = 'batches/add_batch.html'
    context = {}
    if request.method == 'POST':
        form = BatchForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('batches:list_batches')
    form = BatchForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_batches(request):
    template_name = 'batches/list_batches.html'
    batches = Batch.objects.filter()
    context = {
        'batches': batches
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_batch(request, id_batch):
    template_name = 'batches/add_batch.html'
    context ={}
    batch = get_object_or_404(Batch, id=id_batch)
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES,  instance=batch)
        if form.is_valid():
            form.save()
            return redirect('batches:list_batches')
    form = BatchForm(instance=batch)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_batch(request, id_batch):
    batch = Batch.objects.get(id=id_batch)
    batch.delete()
    return redirect('batches:list_batches')