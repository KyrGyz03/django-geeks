from django.shortcuts import render
from cars.models import Car
# Create your views here.


def car_list(request):
    if request.method == 'GET':
        cars = Car.objects.all()
        return render(request, 'cars_list.html', {'cars': cars})