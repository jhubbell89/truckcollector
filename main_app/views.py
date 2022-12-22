from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Truck
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
  service_form = ServiceForm()
  return render(request, 'trucks/detail.html', { 'truck': truck, 'service_form': service_form })

def add_service(request, truck_id):
  form = ServiceForm(request.POST)
  if form.is_valid():
    new_service = form.save(commit=False)
    new_service.truck_id = truck_id
    new_service.save()
  return redirect('detail', truck_id=truck_id)

class TruckCreate(CreateView):
  model = Truck
  fields = '__all__'

class TruckUpdate(UpdateView):
  model = Truck
  fields = ['make', 'model', 'condition', 'year']

class TruckDelete(DeleteView):
  model = Truck
  success_url = '/trucks/'
