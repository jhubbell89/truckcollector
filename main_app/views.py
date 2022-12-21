from django.shortcuts import render
from .models import Truck

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
  return render(request, 'trucks/detail.html', { 'truck': truck })