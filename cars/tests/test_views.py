import json
from rest_framework.test import APITestCase
from django.urls import reverse
from cars.models import Car, Rate



class TestCarView(APITestCase):

    @classmethod
    def setUpTestData(self):
        bmw = Car.objects.create(make='BMW', model='M3')
        toyota = Car.objects.create(make='TOYOTA', model='CAMRY')
        audi = Car.objects.create(make='AUDI', model='Q5')

        Rate.objects.create(rating=5, car_id=bmw)
        Rate.objects.create(rating=5, car_id=bmw)
        Rate.objects.create(rating=3, car_id=toyota)
        Rate.objects.create(rating=2, car_id=toyota)
        Rate.objects.create(rating=2, car_id=toyota)
        Rate.objects.create(rating=3, car_id=toyota)
        Rate.objects.create(rating=4, car_id=audi)
        Rate.objects.create(rating=4, car_id=audi)
        Rate.objects.create(rating=4, car_id=audi)

    def test_cars_list(self):
        url = reverse('cars-list')
        response = self.client.get(url, format='json')
        data_bmw = {
            'id': 1,
            'make': 'BMW',
            'model': 'M3',
            'avg_rating': 5.0
        }
        data_toyota = {
            'id': 2,
            'make': 'TOYOTA',
            'model': 'CAMRY',
            'avg_rating': 2.5
        }
        data_audi = {
            'id': 3,
            'make': 'AUDI',
            'model': 'Q5',
            'avg_rating': 4.0
        }
        self.assertEqual(response.status_code, 200)
        self.assertIn(data_bmw, json.loads(response.content))
        self.assertIn(data_toyota, json.loads(response.content))
        self.assertIn(data_audi, json.loads(response.content))

    def test_car_create(self):
        data_honda = {
            'make': 'Honda',
            'model': 'Accord',
        }
        response = self.client.post('/cars/', data=data_honda)
        url = reverse('cars-list')
        response = self.client.get(url, format='json')
        self.assertEqual(len(json.loads(response.content)), 4)

    def test_car_delete(self):
        response = self.client.delete('/cars/2/')
        response = self.client.get('/cars/')
        data_toyota = {
            'id': 2,
            'make': 'TOYOTA',
            'model': 'CAMRY',
            'avg_rating': 2.5
        }
        self.assertNotIn(data_toyota, json.loads(response.content))

    def test_car_popular(self):
        url = reverse('popular')
        response = self.client.get(url)
        self.assertEqual(json.loads(response.content)[0]['id'], 2)
        self.assertEqual(json.loads(response.content)[1]['id'], 3)
        self.assertEqual(json.loads(response.content)[2]['id'], 1)


class TestRateView(APITestCase):

    @classmethod
    def setUpTestData(self):
        bmw = Car.objects.create(make='BMW', model='M3')
        Rate.objects.create(rating=5, car_id=bmw)
    
    def test_rate_create(self):
        url = reverse('rate')
        data = {
            'car_id': 5,
            'rating': 3
        }
        response = self.client.post(url, data=data)
        url = reverse('cars-list')
        response = self.client.get(url, format='json')
        data_bmw = {
            'id': 5,
            'make': 'BMW',
            'model': 'M3',
            'avg_rating': 4.0
        }
        self.assertIn(data_bmw, json.loads(response.content))

    
