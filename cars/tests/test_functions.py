from django.test import TestCase

from cars.functions import check_if_car_exists


class TestCarExistance(TestCase):

    def test_car_exists(self):
        self.assertTrue(check_if_car_exists('BMW', 'M3'))

    def test_car_does_not_exists(self):
        self.assertFalse(check_if_car_exists('AUDI', 'M3'))