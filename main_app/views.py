from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Truck, Mod
from .forms import ServiceForm

# Create your views here.
def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def trucks_index(request):
  trucks = Truck.objects.all()
  return render(request, 'trucks/index.html', { 'trucks': trucks })

def trucks_detail(request, truck_id):
  truck = Truck.objects.get(id=truck_id)
  id_list = truck.mods.all().values_list('id')
  mods_truck_doesnt_have = Mod.objects.exclude(id__in=id_list)
  service_form = ServiceForm()
  return render(request, 'trucks/detail.html', { 
    'truck': truck, 
    'service_form': service_form, 
    'mods': mods_truck_doesnt_have 
    })

def add_service(request, truck_id):
  form = ServiceForm(request.POST)
  if form.is_valid():
    new_service = form.save(commit=False)
    new_service.truck_id = truck_id
    new_service.save()
  return redirect('detail', truck_id=truck_id)

class TruckCreate(CreateView):
  model = Truck
  fields = ['make', 'model', 'condition', 'year']

class TruckUpdate(UpdateView):
  model = Truck
  fields = ['make', 'model', 'condition', 'year']

class TruckDelete(DeleteView):
  model = Truck
  success_url = '/trucks/'

class ModList(ListView):
  model = Mod

class ModDetail(DetailView):
  model = Mod

class ModCreate(CreateView):
  model = Mod
  fields = '__all__'

class ModUpdate(UpdateView):
  model = Mod
  fields = ['name', 'skill']

class ModDelete(DeleteView):
  model = Mod
  success_url = '/mods/'

def assoc_mod(request, truck_id, mod_id):
  Truck.objects.get(id=truck_id).mods.add(mod_id)
  return redirect('detail', truck_id=truck_id)