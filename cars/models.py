from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator


class User(AbstractUser):
    pass


class Car(models.Model):
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.make} {self.model}'


class Rate(models.Model):
    rating = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    car_id = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'Rate: {self.rating}'