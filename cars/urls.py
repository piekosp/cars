from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import CarViewSet, RateCreate
from .views import GetPopularCars


router = DefaultRouter()
router.register(r'cars', CarViewSet, basename='cars')

urlpatterns = [
    path('', include(router.urls)),
    path('rate/', RateCreate.as_view(), name='rate'),
    path('popular/', GetPopularCars.as_view(), name='popular')
]