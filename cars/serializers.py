from rest_framework import serializers
from django.db.models import Avg
from .models import Car, Rate 
from .functions import check_if_car_exists


class CarListSerializer(serializers.ModelSerializer):

    avg_rating = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'avg_rating']

    def get_avg_rating(self, obj):
        rates = obj.rate_set.all()
        if rates.count():
            return rates.aggregate(Avg('rating')).get('rating__avg')
        return 0


class CarCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['id', 'make', 'model']

    def validate(self, data):
        car_make = data.get('make').upper()
        car_model = data.get('model').upper()
        if check_if_car_exists(car_make, car_model):
            data['make'] = car_make
            data['model'] = car_model
            return super().validate(data)
        else:
            raise serializers.ValidationError("Car does not exist!")

    def create(self, validated_data):
        car, _ = Car.objects.get_or_create(**validated_data)
        return car


class PopularCarsSerializer(serializers.ModelSerializer):

    rates_number = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Car
        fields = ['id', 'make', 'model', 'rates_number']

    def get_rates_number(self, obj):
        rates = obj.rate_set.all()
        return rates.count()


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = ['car_id', 'rating']

