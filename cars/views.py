from rest_framework import generics
from rest_framework import viewsets
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Count
from .serializers import CarListSerializer, CarCreateSerializer, RateSerializer
from .serializers import PopularCarsSerializer
from .models import Car, Rate


class CarViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = Car.objects.all()
        serializer = CarListSerializer(queryset, many=True)
        return Response(serializer.data)

    
    def create(self, request):
        serializer = CarCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def destroy(self, request, pk=None):
        try:
            car = Car.objects.get(id=pk)
            car.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except ObjectDoesNotExist:
            return Response({'error': 'Car does not exist!'}, status=status.HTTP_404_NOT_FOUND)


class GetPopularCars(generics.ListAPIView):
    queryset = Car.objects.all().select_related()
    queryset = queryset.annotate(rates=Count('rate__rating'))
    queryset = queryset.order_by('-rates')
    serializer_class = PopularCarsSerializer


class RateCreate(generics.CreateAPIView):
    queryset = Rate.objects.all()
    serializer_class = RateSerializer