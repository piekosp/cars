from django.contrib import admin
from cars.models import Car
from cars.models import User
from cars.models import Rate


admin.site.register(User)
admin.site.register(Car)
admin.site.register(Rate)



