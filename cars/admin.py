from django.contrib import admin
from cars.models import CategoryCar, Car, StateNum_car, CommentCar
# Register your models here.

admin.site.register(CategoryCar)
admin.site.register(Car)
admin.site.register(StateNum_car)
admin.site.register(CommentCar)

