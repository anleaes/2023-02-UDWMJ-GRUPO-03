from django.shortcuts import render, get_object_or_404, redirect
from .forms import BrandForm
from .models import Brand
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/contas/login/')
def add_brand(request):
    template_name = 'brands/add_brands.html'
    context = {}
    if request.method == 'POST':
        form = BrandForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            form.save_m2m()
            return redirect('brands:list_brands')
    form = BrandForm()
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def list_brands(request):
    template_name = 'brands/list_brands.html'
    brands = Brand.objects.filter()
    context = {
        'brands': brands
    }
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def edit_brands(request, id_brand):
    template_name = 'brands/add_brands.html'
    context ={}
    brand = get_object_or_404(Brand, id=id_brand)
    if request.method == 'POST':
        form = BrandForm(request.POST, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('brands:list_brands')
    form = BrandForm(instance=brand)
    context['form'] = form
    return render(request, template_name, context)

@login_required(login_url='/contas/login/')
def delete_brand(request, id_brand):
    brand = Brand.objects.get(id=id_brand)
    brand.delete()
    return redirect('brands:list_brands')