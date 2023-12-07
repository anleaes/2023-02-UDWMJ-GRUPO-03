from django.shortcuts import render, get_object_or_404, redirect
from .forms import BatchForm
from .models import Batch

# Create your views here.
def add_batch(request):
    template_name = 'batches/add_batch.html'
    context = {}
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('batches:list_batches')
    form = BatchForm()
    context['form'] = form
    return render(request, template_name, context)

def list_batches(request):
    template_name = 'batches/list_batches.html'
    batches = Batch.objects.filter()
    context = {
        'batches': batches
    }
    return render(request, template_name, context)

def edit_product(request, id_product):
    template_name = 'batches/add_product.html'
    context ={}
    product = get_object_or_404(Batch, id=id_product)
    if request.method == 'POST':
        form = BatchForm(request.POST, request.FILES,  instance=product)
        if form.is_valid():
            form.save()
            return redirect('batches:list_batches')
    form = BatchForm(instance=product)
    context['form'] = form
    return render(request, template_name, context)

def delete_product(request, id_product):
    batch = Batch.objects.get(id=id_product)
    product.delete()
    return redirect('batches:list_batches')